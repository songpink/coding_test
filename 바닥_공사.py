n = int(input())

method = [0]*n

method[0] = 1
method[1] = 3

for i in range(2, n):
    method[i] = method[i-2]*2 + method[i-1]

print(method[-1])
