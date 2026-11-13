import pandas as pd

marvel = ['Spider-Man', 'Black Panther', 'Guardians of the Galaxy', 'Deadpool', 'Captain America']

s = pd. Series (marvel)

print (s)
d=pd.Series([0,1,2,3])
print(d*2)
import numpy as np
arr = np.arange(0, 5)

ss = pd.Series(arr)

print (ss)

dates = pd.date_range('2025-01-01', '2025-01-05')

print(dates)

new_s = pd.Series (marvel, index=dates)

print(new_s)


import pandas as pd
import numpy as np

n = np. arange(10, 16)

s = pd.Series(n)

print(s)

np.random.seed(0)

r = np.random.random(size = 6)

s = pd.Series(r)

print(s)

s = pd.Series(4)

print(s)