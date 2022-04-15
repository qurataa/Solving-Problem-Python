# Magnus
letter = input()
h=0
o=0
n=0
i=0
count = 0


for char in letter :
	if char == 'H' and h==0:
		h=1
	elif char == 'O' and h > o:
		o=1
	elif char == 'N' and o > n:
		n=1
	elif char == 'I' and n > i:
		count = count + 1
		h=0
		o=0
		n=0

print (count)