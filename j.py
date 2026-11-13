import pandas as pd
d = {'coll': [1, 2], 'col2': [3, 4]}
df = pd. DataFrame(data=d)
print(df)

df.index = ["new index0", "new index1"]
print(df)

df.columns = ["new_col1", "new_col2"]

print(df)


import pandas as pd
d = {'coll': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)

df.rename(index= {0:"new index0"})