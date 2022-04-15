burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger == 1 :
	b_cal = 461
elif burger == 2:
	b_cal = 431
elif burger == 3:
	b_cal = 420
else :
	b_cal = 0


if side == 1 :
	s_cal = 100
elif side == 2:
	s_cal = 57
elif side == 3:
	s_cal = 70
else :
	s_cal = 0

if drink == 1 :
	d_cal = 130
elif drink == 2:
	d_cal = 160
elif drink == 3:
	d_cal = 118
else :
	d_cal = 0

if dessert == 1 :
	dsrt_cal = 167
elif dessert == 2:
	dsrt_cal = 266
elif dessert == 3:
	dsrt_cal = 75
else :
	dsrt_cal = 0


total_cal = b_cal + s_cal + d_cal + dsrt_cal

print ('Your total Calorie count is '+str(total_cal)+'.')