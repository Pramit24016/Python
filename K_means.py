import pandas as pd
from sklearn.preprocessing import StandardScaler
df=pd.read_csv('Mall_Customers.csv')
df=df.drop_duplicates()
df=df.dropna()
epoch=1000
scalar=StandardScaler()

def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

for i in range(1,epoch):
	k=i
	K_sample_points=df.sample(n=k,replace=False)
	X=df.drop(columns=['CustomerID','Gender'])
	K_samples=K_sample_points.drop(columns=['CustomerID','Gender'])
	X=scalar.fit_transform(X)
	K_samples=scalar.fit_transform(K_samples)
	for i in X:
		
