number_of_parts = int(input())
parts_list = list(map(int, input().split()))
number_of_request = int(input())
request_list = list(map(int, input().split()))

for j in range(number_of_request):
    if request_list[j] in parts_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')
