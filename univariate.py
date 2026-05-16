import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import seaborn as sns
df=pd.read_csv('std_data.csv')
print(f"Avg Age:{df['Age'].mean()}")
print(f"Median of Age:{df['Age'].median()}")
print(f"Mode of Age:{df['Age'].mode()}")
plt.hist(df['Age'])
plt.title('Age-Historgram')
plt.show()
plt.boxplot(df['Age'])
plt.title('Boxplot-Age')
plt.show()
plt.hist(df['Age'].skew())
plt.title('Skewness')
plt.show()
