import pandas as pd
import numpy as np
df=pd.read_csv("binary_10bit_with_value.csv")
df=df.drop_duplicates()
y=df['Decimal_Value'].to_numpy()
X=df.drop(columns='Decimal_Value').to_numpy()
w=[]
weight=np.zeros(10)
for i in range(10):
	x=2**i
	w.append(x)
epoch=1000
alpha=0.01
for k in range(epoch):
	for j in X:
		for i in range(10):
			output=np.sum(weight[i]*X[j][i])
			error=y[j]-output
			weight[i]=weight[i]+(alpha*error*X[j][i])
print(weight)
