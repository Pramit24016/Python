import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('std_data.csv')
plt.boxplot(df['Marks'])
plt.show()
Q1=df['Marks'].quantile(0.25)
Q3=df['Marks'].quantile(0.75)
IQR=Q3-Q1
lb=Q1-(1.5*IQR)
ub=Q3+(1.5*IQR)
outliners=df[(df['Marks']<lb) | (df['Marks']>ub)]
df_clean = df[(df['Marks'] >= lb) & (df['Marks'] <= ub)]
print(df_clean['Marks'])
df['Marks'] = df['Marks'].clip(lb, ub)
