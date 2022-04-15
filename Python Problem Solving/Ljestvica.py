# # Ljestvica
# CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C
note = ['A','B','C','D','E','F','G','|']
Amin = ['A','D','E']
Cmaj = ['C','F','G']
Amin_count = 0
Cmaj_count = 0
notes = []
key=[]


inputt = input()
input_list = inputt.split('|')

if 2 <= len(input_list) <= 100 and '||' not in inputt:
	for char in inputt :
		if char in note:
			key.append(char)

	if key[0] != '|'  and key[-1] != '|':
		for a in range(len(inputt)):
			if a ==0 and key[a] != '|':
				notes.append(key[a])
			elif a != '0' and key[a-1]=='|' and key[a]!= '|' :
				notes.append(key[a])

		for count in notes:
			if count in Amin:
				Amin_count += 1
			elif count in Cmaj:
				Cmaj_count += 1

		if Cmaj_count > Amin_count :
			print ('C-dur')
		elif Cmaj_count < Amin_count :
			print ('A-mol')
		elif Cmaj_count == Amin_count and notes[-1] in Cmaj:
			print ('C-dur')
		elif Cmaj_count == Amin_count and notes[-1] in Amin:
			print ('A-mol')
