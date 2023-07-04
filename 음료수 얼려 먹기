#DFS알고리즘 사용하기
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
result = 0

def dfs(r, c):
    if r<=-1 or r>=n or c<=-1 or c>=m:
        return False

    if graph[r][c] == 0:
        graph[r][c] = 1
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
