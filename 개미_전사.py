n = int(input())
k = list(map(int, input().split()))


foods = [0]*n

foods[0] = k[0]
foods[1] = max(k[1], k[0])

for i in range(2, n):
    foods[i] = max(foods[i-2]+k[i], foods[i-1])

result = foods[-1]
print(result)
