import interest
p=int(input('Enter the Principle value: '))
r=float(input('Enter the rate of interest: '))
t=int(input('Enter the time period of the interest: '))
print(f'Simple Interest:{interest.si(p,r,t)}')
print(f'Compound Interest:{interest.cpi(p,r,t)}')
