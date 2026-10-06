from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv('house_price.csv')
df=df.dropna()
df=df.drop_duplicates()

print(df)
