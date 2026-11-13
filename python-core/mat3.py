import pandas as pd
import matplotlib.pyplot as plt

population_2024 = {
	'New York': 8258000,
	'Los Angeles': 3821000,
	'Chicago': 2665000,
	'Houston': 2310000,
}

population_2025 = {
	'New York': 8270000,
	'Los Angeles': 3830000,
	'Chicago': 2672000,
	'Houston': 2320000,
}

city_area = {
	'New York': 778,
	'Los Angeles': 1302,
	'Chicago': 589,
	'Houston': 1651,
}

s_2024 = pd.Series(population_2024)
s_2025 = pd.Series(population_2025)
s_area = pd.Series(city_area)
growth = s_2025 - s_2024
print(growth)

x=growth. index
y=growth. values
plt.figure(figsize = (13, 6))

plt.xticks(rotation='vertical', size = 10)

plt.barh(x, y)

plt.show()


population_density = s_2024 / s_area

x=population_density.index
y=population_density.values
plt.figure(figsize = (13,6))

plt.xticks(rotation=45, size = 10)

plt.barh(x, y, color='red')

plt.title('population density', size = 15)
plt.ylabel('city', size = 15)
plt.xlabel('population', size = 15)

plt.show()
print('Average population density:', population_density.mean())
print('Maximum population density:', population_density.max())
