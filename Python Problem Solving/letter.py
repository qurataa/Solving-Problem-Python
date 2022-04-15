monthly_mb = int(input('Input Quota Data Monthly : '))
n = int(input('Input how many month will get quota : '))
total_mb = monthly_mb * (n + 1)

for i in range(n):
     used = int(input('Input quota used this '+str(i)+ 'month : '))
     total_mb = total_mb - used

print(total_mb)