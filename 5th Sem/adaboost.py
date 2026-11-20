import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('credit_card.csv').dropna().drop_duplicates()
X = df.drop(columns=['Fraud']).to_numpy()
y = df['Fraud'].apply(lambda x: 1 if x == 1 else -1).to_numpy()

scaler = StandardScaler()
X = scaler.fit_transform(X)

models = [
    LogisticRegression(), 
    SGDClassifier(), 
    SVC(), 
    DecisionTreeClassifier(max_depth=1)
]

N = X.shape[0]
w = np.ones(N) / N
alphas = []
trained_models = []

for model in models:
    model.fit(X, y, sample_weight=w)
    y_pred = model.predict(X)
    
    misclassified = (y_pred != y)
    error = np.sum(w[misclassified]) / np.sum(w)
    
    error = np.clip(error, 1e-10, 1 - 1e-10)
    
    alpha = 0.5 * np.log((1.0 - error) / error)
    
    alphas.append(alpha)
    trained_models.append(model)
    
    w_update = np.where(y_pred == y, np.exp(-alpha), np.exp(alpha))
    w = w_update / np.sum(w) 


preds = np.array([md.predict(X) for md in trained_models])
H = np.sign(np.dot(alphas, preds))

print("Accuracy score:", accuracy_score(y, H))
