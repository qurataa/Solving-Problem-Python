# Uncrackable
passwd = input()
upper = 0
lower = 0
digit = 0

for i in range(len(passwd)):
		if passwd[i].isupper():
			upper = upper + 1
		elif passwd[i].islower():
			lower = lower + 1
		elif passwd[i]>='0' and passwd[i]<='9':
			digit = digit + 1

if (len(passwd) < 8) or (len(passwd) > 12) or (upper < 2) or (lower < 3) or (digit < 1) :
	print('Invalid')
else :
 	print ('Valid')