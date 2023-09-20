x = int(input())

cnt_list = [0]*30001

for i in range(2, x+1):
    
    cnt_list[i] = cnt_list[i-1] + 1

    if i%2 == 0:
        cnt_list[i] = min(cnt_list[i], cnt_list[i//2]+1)
        
    if i%3 == 0:
        cnt_list[i] = min(cnt_list[i], cnt_list[i//3]+1)
        
    if i%5 == 0:
        cnt_list[i] = min(cnt_list[i], cnt_list[i//5]+1)

print(cnt_list[x])
