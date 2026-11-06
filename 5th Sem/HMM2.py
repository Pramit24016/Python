import numpy as np
import pandas as pd

df = pd.read_csv('obv.csv')
Op = df['Observation'].tolist()
S = ['Walking', 'Running', 'Sitting']
V = ['Low', 'Medium', 'High', 'VeryHigh']
Pi = np.array([0.5, 0.3, 0.2])
A = np.array([[0.6, 0.3, 0.1], [0.2, 0.7, 0.1], [0.4, 0.1, 0.5]])
B = np.array([[0.1, 0.6, 0.25, 0.05], [0.02, 0.08, 0.5, 0.4], [0.8, 0.15, 0.04, 0.01]])
sigma_w = []
sigma_r = []
sigma_s = []
state = {}
for i in range(1, 26):
    if i == 1:
        sigma_w.append(Pi[0] * B[0][V.index(Op[i - 1])])
        sigma_r.append(Pi[1] * B[1][V.index(Op[i - 1])])
        sigma_s.append(Pi[2] * B[2][V.index(Op[i - 1])])
        if (sigma_w[i - 1] >= sigma_r[i - 1]) and (sigma_w[i - 1] >= sigma_s[i - 1]):
            state[i] = [Op[i-1],'Walking']
        if (sigma_r[i - 1] >= sigma_w[i - 1]) and (sigma_r[i - 1] >= sigma_s[i - 1]):
            state[i] = [Op[i-1],'Running']
        if (sigma_s[i - 1] >= sigma_w[i - 1]) and (sigma_s[i - 1] >= sigma_r[i - 1]):
            state[i] = [Op[i-1],'Sitting']
    else:
        sigma_w.append(B[0][V.index(Op[i - 1])] * max((A[0][0] * sigma_w[i - 2]), (A[1][0] * sigma_r[i - 2]), (A[2][0] * sigma_s[i - 2])))
        sigma_r.append(B[1][V.index(Op[i - 1])] * max((A[0][1] * sigma_w[i - 2]), (A[1][1] * sigma_r[i - 2]), (A[2][1] * sigma_s[i - 2])))
        sigma_s.append(B[2][V.index(Op[i - 1])] * max((A[0][2] * sigma_w[i - 2]), (A[1][2] * sigma_r[i - 2]), (A[2][2] * sigma_s[i - 2])))
        if (sigma_w[i - 1] >= sigma_r[i - 1]) and (sigma_w[i - 1] >= sigma_s[i - 1]):
            state[i] = [Op[i-1],'Walking']
        if (sigma_r[i - 1] >= sigma_w[i - 1]) and (sigma_r[i - 1] >= sigma_s[i - 1]):
            state[i] = [Op[i-1],'Running']
        if (sigma_s[i - 1] >= sigma_w[i - 1]) and (sigma_s[i - 1] >= sigma_r[i - 1]):
            state[i] = [Op[i-1],'Sitting']

for key,values in state.items():
	print(f'{key}: {values}')
