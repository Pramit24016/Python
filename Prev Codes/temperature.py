def celcius(f):
	c=5*(f-32)
	c=c/9
	return c
def fahrenheit(cel):
	f=((9*cel)/5)+32
	return f
def c_k(cel):
	kel=cel+273
	return kel
def f_k(f):
	c=celcius(f)
	kel=c_k(c)
	return kel
def k_c(k):
	c=k-273
	return c
def k_f(k):
	cel=k_c(k)
	f=fahrenheit(cel)
	return f
