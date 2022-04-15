P = int(input())
B = int(input())
D = int(input())

cap = P // B
paint = P % B

cap_dolar = cap * D
total = cap_dolar + paint
print (total)