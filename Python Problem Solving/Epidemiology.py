# Epidemiology
day=0
total =0

target = int(input())
p_infected = int(input())
grow = int(input())

if grow <= 10 and p_infected <= target and target < 10000000:
	while total < target :
		day = day + 1
		total = total + p_infected
		p_infected = p_infected * grow

	print (f'{day -1 }')

