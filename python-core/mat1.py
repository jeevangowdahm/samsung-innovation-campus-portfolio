import matplotlib.pyplot as plt

x = range(100)
y = [value ** 2 for value in x]

plt.plot(x,y, linewidth=8.0, color='blue')

plt.title('hello world of chart')
plt.ylabel('y-some numbers')
plt.xlabel('x-some numbers')

plt.show()