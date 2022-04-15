# Multiple Choice

num = int(input())
answer=[]
correct=[]
poin = 0
for a in range(num):
	answer.append(input())

for c in range(num):
	correct.append(input())

for cek in range(num):
	if answer[cek] == correct[cek] :
		poin +=1

print (poin)