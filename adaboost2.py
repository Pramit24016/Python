import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
df = pd.read_csv('credit_card.csv').dropna().drop_duplicates()
X = df.drop(columns=['Fraud']).to_numpy()
y = df['Fraud'].apply(lambda x: 1 if x == 1 else -1).to_numpy() 

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models = [LogisticRegression(), SGDClassifier(), SVC(probability=True), DecisionTreeClassifier(max_depth=1)]

N = X_train.shape[0]
w = np.ones(N) / N
alphas = []
trained_models = []

for model in models:
    model.fit(X_train, y_train, sample_weight=w)
    y_pred = model.predict(X_train)
    misclassified = (y_pred != y_train)
    error = np.sum(w[misclassified])
    if error == 0:
        alpha = 1.0
    else:
        alpha = 0.5 * np.log((1 - error) / error)
    alphas.append(alpha)
    trained_models.append(model)
    w_update = np.where(y_pred == y_train, np.exp(-alpha), np.exp(alpha))
    w = w * w_update
    w = w / np.sum(w)
final_pred=[]
for i,md in enumerate(models):
	md.fit(X_train,y_train,sample_weight=w,random_state=0)
	y_pred=m.predict(X_test)
	final_pred.append(alphas[i]*y_pred)

print(f"Accuracy:{accuracy_score(final_pred,y_test)}")
