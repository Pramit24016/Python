import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')
df = df.drop_duplicates()
df = df.dropna()

X = df.drop(columns=['CustomerID', 'Gender'])
scaler = StandardScaler()
X = scaler.fit_transform(X)


def dist(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


def kmeans(X, k, iters=100):
    idx = np.random.choice(X.shape[0], size=k, replace=False)
    c = X[idx]

    for _ in range(iters):
        groups = [[] for _ in range(k)]
        y = np.zeros(X.shape[0], dtype=int)

        for i, x in enumerate(X):
            dists = [dist(x, cent) for cent in c]
            best_k = np.argmin(dists)
            groups[best_k].append(x)
            y[i] = best_k

        new_c = np.zeros((k, X.shape[1]))
        for i, pts in enumerate(groups):
            if len(pts) > 0:
                new_c[i] = np.mean(pts, axis=0)
            else:
                new_c[i] = c[i]

        if np.all(c == new_c):
            break
        c = new_c

    wcss = 0
    for i, x in enumerate(X):
        wcss += np.sum((x - c[y[i]]) ** 2)

    return wcss


scores = []
max_k = 10

for k in range(1, max_k + 1):
    w = kmeans(X, k)
    scores.append(w)
    print(f"K = {k}, WCSS = {w:.2f}")

plt.figure(figsize=(8, 5))
plt.plot(range(1, max_k + 1), scores, marker='o', linestyle='--', color='b')
plt.title('Elbow Method')
plt.xlabel('K')
plt.ylabel('WCSS')
plt.xticks(range(1, max_k + 1))
plt.grid(True)
plt.show()