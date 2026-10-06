import pandas as pd
df=pd.read_csv('std_data.csv')
print(df.head(5))
print(df.tail(5))
print(f'shape:{df.shape}')
print(f'Column names:{df.info()}')
print(f'Description:{df.describe()}')

