# Special Day

month = int(input())
date = int(input())

if month == 2 :
	if date < 18 :
		print ('Before')
	elif date > 18 :
		print ('After')
	elif date == 18 :
		print ('Special')
elif month < 2:
	print ('Before')
elif month > 2:
	print ('After')
