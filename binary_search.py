def binary_search(array, target):
    start, end = 0, len(array)-1
    
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search([1, 3, 5, 6, 8, 10, 23, 40, 100, 451, 2312], 23)

print(result)
