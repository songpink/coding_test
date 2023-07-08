#선택정렬 Selection Sort
array = [4, 5, 1, 8, 7, 6, 0, 9, 2, 3]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
