import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('credit_card.csv')
df = df.dropna()
df = df.drop_duplicates()
df_y = df['Fraud']
df_X = df.drop(columns=['Fraud'])
X = df_X.to_numpy()
y = df_y.to_numpy()
y = 2 * y - 1
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

eta = 0.001
C = 1
T = 100

n_samples, d_features = X_train.shape
w = np.zeros(d_features)
b = 0

for epoch in range(T):
    for i in range(n_samples):
        x_i = X_train[i]
        y_i = y_train[i]
        
        if y_i * (np.dot(w, x_i) + b) < 1:
            w = w - eta * (2 * w - C * y_i * x_i)
            b = b + eta * C * y_i
        else:
            w = w - eta * (2 * w)

pred_val = np.dot(X_test, w) + b
predictions = np.where(pred_val < 0, -1, 1)

accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")
