def si(p,r,t):
	i=(p*(r/100))*t
	return i
def cpi(p,r,t):
	i=(p*((1+r/100)**t))-p
	return i
