n = int(input())
sum = 0
for n in range(1, n):
    sum += 1 / (2 ** n)
print(sum)
