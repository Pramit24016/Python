import pandas as pd
df=pd.read_csv("std_data.csv")
df1=df[["StudentID","StudyHours","Attendance","Marks"]].copy()
df1.loc[:,'Internal Marks']=df1['Marks']*0.25
df1.loc[:,'Final Marks']=df1['Marks']
df1=df1.drop(columns="Marks")
df1=df1.dropna()
print(f'Number of rows:{df1.shape[0]}\nNumber of columns:{df1.shape[1]}\n\n')
print(df1.info())
print('\n\nNumber of duplicate data:',df1.duplicated().sum())
print('\n\nFirst 5 rows:\n',df1.head(5))
print('\n\nLast 5 rows:\n',df1.tail(5))
