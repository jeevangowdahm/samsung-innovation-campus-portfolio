import pandas as pd

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'D', 'c', 'd']}
df = pd.DataFrame(data)

print(df)


import pandas as pd
s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
s2 = pd.Series ([1.0, 2.0, 3.0, 4.0], index=["a","b","c", "d"])

data = {"one":s, "two":s2}

pd.DataFrame(data)