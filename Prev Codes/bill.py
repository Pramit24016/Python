def item_cost(cost):
	a=int(input('Enter the cost of the item:'))
	cost.append(a)
def discount(cost,d):
	for i in range(0,len(cost)):
		cost[i]=cost[i]-(cost[i]*(d/100))
def total(cost):
	return sum(cost)
