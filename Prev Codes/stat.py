def mean(list):
	s=sum(list)
	l=len(list)
	m=s/l
	return m
def median(list):
	list.sort()
	l=len(list)
	if l%2!=2:
		n=(l+1)/2
		n1=int(n)
		return list[n1-1]
	else:
		n1=l/2
		n2=(l/2)+1
		n3=int(n1)
		n4=int(n2)
		median=(list[n3-1]+list[n4-1])/2
		return median
def mode(list):
	dict={}
	for i in list:
		dict[i]=dict.setdefault(i,0)+1
	max=-1
	for k,v in dict.items():
		if v>max:
			max=v
			mode=k
	return mode

