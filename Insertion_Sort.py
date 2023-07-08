arr = [7, 5, 6, 9, 3, 2, 0, 1, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[i], arr[j-1] = arr[j-1], arr[i]
        else:
            break

print(arr)
