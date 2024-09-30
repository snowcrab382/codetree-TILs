from copy import deepcopy
from collections import deque

# input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(graph):
    global fire

    q = deque(fire)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                graph[nx][ny] = 2
                q.append((nx,ny))
    cnt = 0
    for i in graph:
        for j in i:
            if not j:
                cnt += 1
    return cnt

fire = []
candidate = []
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            candidate.append((i,j))
        if graph[i][j] == 2:
            fire.append((i,j))

result = 0
leng = len(candidate) 
for i in range(leng):  
    for j in range(i + 1, leng):
        for k in range(j + 1, leng):
            tmp = deepcopy(graph)
            a, b, c = candidate[i], candidate[j], candidate[k]
            tmp[a[0]][a[1]] = 1
            tmp[b[0]][b[1]] = 1
            tmp[c[0]][c[1]] = 1
            result = max(result, check(tmp))
print(result)