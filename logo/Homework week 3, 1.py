a = input().split()   # список строк
n = 0
for i in range(1, len(a)-1):
    if int(a[i-1]) < int(a[i]) and int(a[i]) > int(a[i+1]):
        n += 1
print(n)
