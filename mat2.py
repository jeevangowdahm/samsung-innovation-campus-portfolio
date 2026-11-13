from matplotlib import pyplot as plt
days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553,1000000,2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]
plt.bar(range(len(days_in_year)), days_in_year)
plt.show()