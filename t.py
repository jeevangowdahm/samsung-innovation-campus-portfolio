import matplotlib.pyplot as plt
import pandas_datareader as pdr
df = pdr.get_data_fred('GS10')

print(df.shape)

print(df.head)
plt.plot(df)
plt.show()

df1= pdr.get_data_famafrench("F-F_Research_Data_Factors")


print(df1)
plt.plot(str(df1))
plt.show()