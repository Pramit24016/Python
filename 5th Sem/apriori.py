import pandas as pd
import numpy as np
import ast
from itertools import combinations

def support(item,trn_list):
	count=0
	for i in trn_list:
		if item in i:
			count=count+1
	return count

def itemset_support(itemset,trn_list):
	count=0
	for i in trn_list:
		if set(itemset).issubset(set(i)):
			count=count+1
	return count

minSup=0.3
minConf=0.6
df=pd.read_csv('trn.csv')
row,col=df.shape
df['Items'] = df['Items'].apply(ast.literal_eval)
unique=[]
for i in df['Items']:
	for k in i:
		if k not in unique:
			unique.append(k)
c1=unique
c1_supportCount=[]
for i in unique:
	c1_supportCount.append(support(i,df['Items']))
c1_support=[x/row for x in c1_supportCount]

l1=[]
frequent_itemsets={}
for i in range(len(c1)):
	if c1_support[i]>=minSup:
		l1.append([c1[i]])
		frequent_itemsets[tuple([c1[i]])]=c1_support[i]

k=2
lk=l1
while lk:
	ck=[]
	for i in range(len(lk)):
		for j in range(i+1,len(lk)):
			cand=sorted(list(set(lk[i])|set(lk[j])))
			if len(cand)==k and cand not in ck:
				subs=list(combinations(cand,k-1))
				if all(sorted(list(s)) in lk for s in subs):
					ck.append(cand)
	lk_next=[]
	for cand in ck:
		sup=itemset_support(cand,df['Items'])/row
		if sup>=minSup:
			lk_next.append(cand)
			frequent_itemsets[tuple(cand)]=sup
	lk=lk_next
	k+=1

rules=[]
for itemset,sup in frequent_itemsets.items():
	if len(itemset)>1:
		for i in range(1,len(itemset)):
			for ant in combinations(itemset,i):
				cons=tuple(sorted(set(itemset)-set(ant)))
				ant_sup=frequent_itemsets[tuple(sorted(ant))]
				conf=sup/ant_sup
				if conf>=minConf:
					rules.append((list(ant),list(cons),round(sup,4),round(conf,4)))

print("Frequent Itemsets:")
for itemset,sup in frequent_itemsets.items():
	print(f"{list(itemset)}: {round(sup,4)}")

print("\nAssociation Rules:")
for ant,cons,sup,conf in rules:
	print(f"{ant} -> {cons} | Support: {sup}, Confidence: {conf}")
