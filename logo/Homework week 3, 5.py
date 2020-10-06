a = list(set([int(j) for j in input().split()]) & set([int(j) for j in input().split()]))  # найдем пересечение множеств
for elem in sorted(a):  # выведем в порядке возрастания
    print(elem, end=' ')
