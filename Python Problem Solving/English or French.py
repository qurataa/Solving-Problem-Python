# English or French?
word =''
T=0
S=0

num_line = int(input())

for line in range(num_line) :
	word += input()

for char in word :
	if char == 't' or char =='T':
		T+=1
	if char == 's' or char =='S':
		S+=1

if T > S :
	print ('English')
elif T < S :
	print ('French')
elif T == S :
	print ('French')

