# Riječi
# A->B B->BA
#BA-> BAB -> BABBA -> BABBABAB
# new_A = number_B

# new_B = number_B and number_A
n=1
A= 1
B=0

button = int(input())
if button <=45 and button >=1:
	while n <= button :
		bnew = 0
		bneww = 0
		anew =0
		
		bneww = A
		bnew = B
		anew = B

		A= anew
		B = bnew + bneww


		n +=1


	print (str(A)+' '+str(B))
