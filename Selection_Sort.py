#선택정렬 Selection Sort
arr = [4, 5, 1, 8, 7, 6, 0, 9, 2, 3]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
