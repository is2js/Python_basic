import pandas as pd

df = pd.DataFrame([
    [1,2,3],
    [4,5,6]
], columns = ['a', 'b', 'c'], index = ['x', 'y'])

df['d'] = df['a'] - df['b']

df = df.append(df.sum(), ignore_index=True)
df.index = ['x', 'y', 'Total']
print(df)