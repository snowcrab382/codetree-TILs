import sys
MAX_NUM = sys.maxsize

# input
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# solution
def calc():
    sum_morning = sum([graph[i][j] for i in range(n) for j in range(n) if not evening[i] and not evening[j]])
    sum_evening = sum([graph[i][j] for i in range(n) for j in range(n) if evening[i] and evening[j]])
    return abs(sum_morning - sum_evening)

def find_min(curr_idx, cnt):
    global answer

    if cnt == n // 2:
        answer = min(answer, calc())
        return
    
    if curr_idx == n:
        return
    
    find_min(curr_idx + 1, cnt)

    evening[curr_idx] = True
    find_min(curr_idx + 1, cnt + 1)
    evening[curr_idx] = False

evening = [False] * n
answer = MAX_NUM
find_min(0, 0)
print(answer)