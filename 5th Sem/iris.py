from sklearn.datasets import load_iris
import pandas as pd
iris=load_iris()
X=iris.data
y=iris.target
print(X.shape)
print(y.shape)
X=pd.DataFrame(X)
print(X.describe())
