import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import date, datetime, time, timezone

df = pd.read_csv("covid-vaccination-doses-per-capita.csv")
df.info()
df['Date'] = pd. to_datetime(df['Day'])
df.set_index('Date', inplace= True)
df.drop(['Day'], axis=1, inplace=True)

print(df.head())

len (df['Entity'].unique())

covid_c = df.groupby(['Entity'])
# Separate the information of the created group by key and print them.
for key, group in covid_c:
    print('+key:', key)
    print('+number:', len(group))
    print(group. head())
    print('\n')

total_df = covid_c[['total_vaccinations_per_hundred' ]].sum()
print(total_df.head())