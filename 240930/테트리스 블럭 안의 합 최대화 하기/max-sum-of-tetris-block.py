#input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 4 X 4 범위 내에서 최대값 구하기
def check():
    global result
    # 길이가 4인 직선 체크 
    for i in range(4):
        result = max(result,sum(reduced[i]))

    comb = [(0,1), (0,2), (0,3), (0,5), (1,2), (2,3), (2,5), (3,4), (3,5), (4,5)]
    # 2 X 3 도형 중 2개를 뺀 것들 중 최대 체크(2,5번 사용 케이스는 제외)
    for i in range(3):
        for j in range(2):
            blocks = []
            for a in range(i, i + 2):
                for b in range(j, j + 3):
                    blocks.append(reduced[a][b])
            tmp_blocks_sum = 100000000
            for x, y in comb:
                tmp_blocks_sum = min(tmp_blocks_sum, blocks[x] + blocks[y])
            result = max(result, sum(blocks) - tmp_blocks_sum)

# 2차원 배열 90도 회전
def rotate(graph):
    return list(map(list, zip(*graph[::-1])))

# 4 X 4로 탐색범위 좁히기
reduced = [[0] * 4 for _ in range(4)]
MAX = 0
for i in range(n - 3):
    for j in range(m - 3):
        tmp = [[0] * 4 for _ in range(4)]
        cnt = 0
        for x in range(4):
            for y in range(4):
                tmp[x][y] = graph[i + x][j + y]
                cnt += tmp[x][y]
        if cnt > MAX:
            MAX = cnt
            reduced = tmp

result = 0
check()
reduced = rotate(reduced)
check()    

print(result)