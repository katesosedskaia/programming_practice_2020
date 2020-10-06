a = [int(s) for s in input().split()]  # преобразованный список чисел
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:  # элемент существует единственный
            break
    else:
        print(a[i], end=' ')
