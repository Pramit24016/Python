import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
df=pd.read_csv('credit_card.csv')
df=df.dropna()
df=df.drop_duplicates()
df_y=df['Fraud']
df_X=df.drop(columns=['Fraud'])
X=df_X.to_numpy()
y=df_y.to_numpy()
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.fit(X_test)
print(X_train.shape)
models=[]
log_reg=LogisticRegression()
models.append(log_reg)
sgd=SGDClassifier()
models.append(sgd)
svc=SVC()
models.append(svc)
dec_tree=DecisionTreeClassifier()
models.append(dec_tree)
ini_w=[1/7 for x in range(7)]
w=[]
for i in range(4):
	if i==0:
		w=ini_w
	model=models[i]
	model.fit(X_train,y_train,max_iters=1,sample_weight=w)
	y_pred=model.predict(X_test)
	incorrect_indices=np.where(y_pred!=y_test)[0]
	X_incorrect=X_test[incorrect_indices]
	feature_weights=model.coef_
	inc_w=feature_weights[incorrect_indices]
	test=inc_w
