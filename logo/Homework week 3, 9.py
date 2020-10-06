counter = {}
for i in range(int(input())):
    s = input().split()  # строка слов
    for a in s:
        counter[a] = counter.get(a, 0) + 1
max_count = max(counter.values())
q = [k for k, v in counter.items() if v == max_count]  # встречается чаще всего
print(min(q))  # меньше в лексикографическом порядке
