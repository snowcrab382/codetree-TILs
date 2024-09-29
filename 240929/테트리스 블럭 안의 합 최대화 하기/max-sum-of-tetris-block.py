#input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

def check(x, y, b):
    global result

    if b == 0:
        if y + 3 < m:
            result = max(result, sum(graph[x][y:y + 4]))
    elif b == 1:
        if x + 1 < n and y + 1 < m:
            result = max(result, graph[x][y] + graph[x][y+1] + graph[x+1][y] + graph[x+1][y+1])
    elif b == 2:
        if x + 2 < n and y + 1 < m:
            result = max(result, graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+2][y+1])
    elif b == 3:
        if x + 2 < n and y + 1 < m:
            result = max(result, graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y+1])
    else:
        if x + 2 < n and y + 1 < m:
            result = max(result, graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y])

for i in range(n):
    for j in range(m):
        for b in range(5):
            check(i, j, b)
print(result)