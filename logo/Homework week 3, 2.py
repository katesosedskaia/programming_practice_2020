a = [int(s) for s in input().split()]  # преобразованый список чисел
min_element = 0
max_element = 0
for i in range(1, len(a)):
    if a[i] > a[max_element]:
        max_element = i
    if a[i] < a[min_element]:
        min_element = i
a[min_element], a[max_element] = a[max_element], a[min_element]   # поменяем местами минимальный и максимальный элементы
print(' '.join([str(i) for i in a]))   # выведем список строк
