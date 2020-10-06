n = [int(s) for s in input().split()]  # преобразованный список чисел
a = set()  # встречались ранее
for i in n:
    if i in a:
        print('YES')
    else:
        print('NO')
        a.add(i)
