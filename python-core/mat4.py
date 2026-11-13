from pathlib import Path
import sys
from typing import Sequence

import pandas as pd


DATA_FILE = (
	Path(sys.argv[1])
	if len(sys.argv) > 1
	else Path(__file__).with_name('TV_Sales.csv')
)


def find_column(
	dataframe: pd.DataFrame,
	names: Sequence[str],
	required: bool = True,
) -> str | None:
	columns = {column.lower().replace(' ', '_'): column for column in dataframe.columns}
	for name in names:
		if name in columns:
			return columns[name]
	if required:
		expected = ', '.join(names)
		raise ValueError(f'Missing one of [{expected}]. Available columns: {list(dataframe.columns)}')
	return None


if DATA_FILE.exists():
	sales_data = pd.read_csv(DATA_FILE)
	print(f'Loaded dataset: {DATA_FILE}')
elif len(sys.argv) > 1:
	raise FileNotFoundError(f'Could not find the supplied dataset: {DATA_FILE}')
else:
	print('TV_Sales.csv was not found; using built-in demo data.')
	sales_data = pd.DataFrame({
		'Brand': ['Vision', 'Vision', 'Nova', 'Nova', 'Apex', 'Apex'],
		'Model': ['V55', 'V65', 'N43', 'N75', 'A50', 'A70'],
		'Screen_Size': [55, 65, 43, 75, 50, 70],
		'Resolution': ['4K', '4K', 'Full HD', '8K', '4K', '8K'],
		'Smart_TV': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes'],
		'Price': [650, 950, 380, 1800, 500, 1500],
		'Sales': [240, 180, 310, 60, 150, 85],
		'Rating': [4.4, 4.6, 4.1, 4.7, 3.8, 4.5],
	})
sales_data.columns = [column.strip() for column in sales_data.columns]

brand_column = find_column(sales_data, ['brand', 'manufacturer', 'make'])
model_column = find_column(sales_data, ['model', 'product', 'product_name'])
price_column = find_column(sales_data, ['price', 'selling_price', 'sale_price'])
sales_column = find_column(sales_data, ['sales', 'units_sold', 'quantity'])
size_column = find_column(sales_data, ['screen_size', 'screen_size_inches', 'size'], required=False)
resolution_column = find_column(sales_data, ['resolution', 'display_resolution'], required=False)
smart_column = find_column(sales_data, ['smart_tv', 'smart', 'smart_feature'], required=False)
rating_column = find_column(sales_data, ['customer_rating', 'rating', 'review_score'], required=False)

assert brand_column is not None
assert model_column is not None
assert price_column is not None
assert sales_column is not None

sales_data[price_column] = pd.to_numeric(sales_data[price_column], errors='coerce')
sales_data[sales_column] = pd.to_numeric(sales_data[sales_column], errors='coerce')
sales_data = sales_data.dropna(subset=[price_column, sales_column]).copy()
sales_data['revenue'] = sales_data[price_column] * sales_data[sales_column]

print('\nTV SALES OPPORTUNITY ANALYSIS')
print(f'Products analysed: {len(sales_data)}')
print(f'Total units sold: {sales_data[sales_column].sum():,.0f}')
print(f'Total revenue: {sales_data["revenue"].sum():,.2f}')

brand_summary = (
	sales_data.groupby(brand_column)
	.agg(units_sold=(sales_column, 'sum'), revenue=('revenue', 'sum'), average_price=(price_column, 'mean'))
	.sort_values('revenue', ascending=False)
)
print('\nTop brands by revenue:')
print(brand_summary.head(10).round(2))

feature_columns = [column for column in [size_column, resolution_column, smart_column] if column]
for feature_column in feature_columns:
	feature_summary = (
		sales_data.groupby(feature_column)
		.agg(units_sold=(sales_column, 'sum'), revenue=('revenue', 'sum'), average_price=(price_column, 'mean'))
		.sort_values('revenue', ascending=False)
	)
	print(f'\nPerformance by {feature_column}:')
	print(feature_summary.round(2))

if rating_column:
	sales_data[rating_column] = pd.to_numeric(sales_data[rating_column], errors='coerce')
	print('\nRelationship between rating and units sold:')
	print(sales_data[[rating_column, sales_column]].corr().round(2))

opportunities = sales_data.sort_values(['revenue', sales_column], ascending=[False, False])
print('\nHighest-revenue products:')
print(opportunities[[brand_column, model_column, price_column, sales_column, 'revenue']].head(10).round(2))

print('\nBusiness insight: prioritise inventory and advertising for the feature combinations '
	  'with the highest revenue, then review high-priced products with low unit sales '
	  'for discounts or repositioning.')
