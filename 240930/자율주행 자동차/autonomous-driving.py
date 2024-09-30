from collections import deque

# input
n, m = map(int,input().split())
x, y, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]

visited[x][y] = 1
q = deque([(x, y, d)])

while q:
    a, b, dir = q.popleft()
    for _ in range(4):
        dir = (dir + 4 - 1) % 4
        nx = a + dx[dir]
        ny = b + dy[dir]
        if graph[nx][ny] != 1 and not visited[nx][ny]:
            visited[nx][ny] = 1
            q.append((nx, ny, dir))
            break
    if not q:
        nx = a - dx[dir]
        ny = b - dy[dir]
        if graph[nx][ny] != 1:
            q.append((nx,ny, dir))

result = 0
for i in visited:
    result += sum(i)
print(result)