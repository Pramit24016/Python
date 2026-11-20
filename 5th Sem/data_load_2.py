import pandas as pd
df=pd.read_csv("std_data.csv")
df1=df[["StudentID","StudyHours","Attendance","Marks"]].copy()
df1.loc[:,'Internal Marks']=df1['Marks']*0.25
df1.loc[:,'Final Marks']=df1['Marks']
df1=df1.drop(columns="Marks")
df1=df1.dropna()
print(df1.describe())
