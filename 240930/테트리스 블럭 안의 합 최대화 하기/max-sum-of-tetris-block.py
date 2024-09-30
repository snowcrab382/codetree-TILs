n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

blocks = [[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],		#연속 일자 모형
		[(0,1),(1,0),(1,1)],							#정사각형
        [(1,0),(1,1),(2,0)],[(1,0),(2,0),(1,-1)],[(0,1),(0,2),(-1,1)],[(0,1),(0,2),(1,1)],	#가운데 툭튀 형
        [(1,0),(1,1),(2,1)],[(1,0),(0,1),(-1,1)],[(0,1),(-1,1),(-1,2)],[(0,1),(1,1),(1,2)],	#계단형
        [(1,0),(2,0),(2,1)],[(0,1),(-1,1),(-2,1)],[(0,1),(1,0),(2,0)],[(0,1),(1,1),(2,1)],	#ㄱ,ㄴ 형
        [(0,1),(0,2),(-1,2)],[(1,0),(1,1),(1,2)],[(0,1),(0,2),(1,2)],[(0,1),(0,2),(1,0)]]


answer = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            tmp = graph[i][j]
            flag = True
            for dx, dy in block:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    tmp += graph[nx][ny]
                else:
                    flag = False
                    break
            if flag:
                answer = max(answer, tmp)
print(answer)