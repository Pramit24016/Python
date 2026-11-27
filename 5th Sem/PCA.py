import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
df=pd.read_csv('wine_data.csv')
df=df.dropna()
df=df.drop_duplicates()
X=df.drop('class',axis=1).to_numpy()
y=df['class'].to_numpy()
scalar=StandardScaler()
X=scalar.fit_transform(X)
covar=np.cov(X,rowvar=False)
eigenvalues,eigenvectors=np.linalg.eigh(covar)
sortedInd=np.argsort(eigenvalues)[::-1]
eigenvalues=eigenvalues[sortedInd]
eigenvectors=eigenvectors[:,sortedInd]
k=int(input("Enter the value of k(max 13): "))
W=eigenvectors[:,:k]
Z=np.dot(X,W)
print(Z)
