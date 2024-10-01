from collections import deque

# input
r, c, k = map(int,input().split())
graph = [[[0, 0] for _ in range(c)] for _ in range(r + 3)]
golems = [] # [출발하는 열, 방향]
for _ in range(k):
    ci, d = map(int, input().split())
    golems.append((ci-1, d)) # 배열외 왼쪽 맨 위가 1,1이기 때문


# functions

# 골렘 이동
def move(g, dir):
    for x, y in g:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= r + 3 or ny < 0 or ny >= c or graph[nx][ny][0]:
            return False

    for i in range(5):
        g[i][0] += dx[dir]
        g[i][1] += dy[dir]
    return True

# 그래프에 위치 기록
def paint(g, exit):
    global graph

    for x, y in g:
        graph[x][y][0] = golem_cnt
    exit_x, exit_y = g[exit][0], g[exit][1]
    graph[exit_x][exit_y][1] = -1

# 정령 이동
def wisp_move(i, j, graph):
    global cnt

    q = deque([(i, j, graph[i][j][0])])
    visited = [[0] * c for _ in range(r + 3)]
    visited[i][j] = 1
    MAX = 0
    while q:
        x, y, golem = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < r + 3 and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny][0]:
                # 다른 골렘인데 현재 위치가 출구가 아니면 스킵
                if golem != graph[nx][ny][0] and graph[x][y][1] != -1:
                    continue
                MAX = max(MAX, nx)
                visited[nx][ny] = 1
                q.append((nx, ny, graph[nx][ny][0]))

    cnt += MAX - 2
                    

# 골렘 스타트
def golem_move(x, y, exit):
    global cnt, golem_cnt, graph

    g = [[x-1,y], [x, y+1], [x+1, y], [x,y-1], [x,y]]
    
    # 아래로 무한 이동
    while True:
        if not move(g, down):
            break
    
    # 최남단에 닿았을 때
    if g[2][0] == r + 2:
        paint(g, exit)
        cnt += r
        return 
    
    # 왼쪽으로 이동
    while True:
        if not move(g, left):
            break
        exit = (exit + 3) % 4
        while True:
            if not move(g, down):
                break

    # 오른쪽으로 이동
    while True:
        if not move(g, right):
            break
        exit = (exit + 1) % 4
        while True:
            if not move(g, down):
                break
    
    # 이동이 끝나도 모든 x좌표중 3 미만인 게 있다면 전체 초기화
    for x, y in g:
        if x < 3:
            graph = [[[0, 0] for _ in range(c)] for _ in range(r + 3)]
            return

    # 최종 위치 표시
    paint(g, exit)
    wisp_move(g[4][0], g[4][1], graph)
        

# solution

# up(0), right(1), down(2), left(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
up, right, down, left = 0, 1, 2, 3
cnt, golem_cnt = 0, 0

for a, b in golems:
    golem_cnt += 1
    golem_move(1, a, b)
print(cnt)