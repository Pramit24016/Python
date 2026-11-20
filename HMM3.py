import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv('obv.csv')
Op = df['Observation'].tolist()

S = ['Walking', 'Running', 'Sitting']
V = ['Low', 'Medium', 'High', 'VeryHigh']

Pi = np.array([0.5, 0.3, 0.2])
A = np.array([[0.6, 0.3, 0.1], 
              [0.2, 0.7, 0.1], 
              [0.4, 0.1, 0.5]])
B = np.array([[0.1, 0.6, 0.25, 0.05], 
              [0.02, 0.08, 0.5, 0.4], 
              [0.8, 0.15, 0.04, 0.01]])

T = len(Op)
N = len(S)

# Viterbi DP table and backpointer table
viterbi = np.zeros((N, T))
backpointer = np.zeros((N, T), dtype=int)

# 1. Initialization Step (t = 0)
first_obs_idx = V.index(Op[0])
for s in range(N):
    viterbi[s, 0] = Pi[s] * B[s, first_obs_idx]
    backpointer[s, 0] = 0

# 2. Recursion Step (t = 1 to T-1)
for t in range(1, T):
    obs_idx = V.index(Op[t])
    for s in range(N):
        prob = viterbi[:, t - 1] * A[:, s] * B[s, obs_idx]
        viterbi[s, t] = np.max(prob)
        backpointer[s, t] = np.argmax(prob)

# 3. Path Backtracking Step
best_path_prob = np.max(viterbi[:, -1])
best_last_state = np.argmax(viterbi[:, -1])

best_path = [best_last_state]
for t in range(T - 1, 0, -1):
    best_last_state = backpointer[best_last_state, t]
    best_path.insert(0, best_last_state)

# Map indices back to state names
most_likely_states = [S[idx] for idx in best_path]
print(most_likely_states)
