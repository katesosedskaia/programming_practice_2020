a = set()  # список слов
for _ in range(int(input())):
    a.update(input().split())
print(len(a))
