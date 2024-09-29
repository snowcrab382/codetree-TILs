from collections import deque
import copy

# input
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate(graph):
    list_of_tuples = zip(*graph[::-1])
    return [list(e) for e in list_of_tuples]

def move(dir, graph):
    # rotate
    for time in dir:
        for _ in range(time):
            graph = rotate(graph)

        # move
        result = []
        for r in graph:
            cnt = 0
            tmp = 0
            tmp_r = deque([])
            for b in r[::-1]:
                if not b:
                    cnt += 1
                    continue

                if tmp != b:
                    tmp_r.appendleft(b)
                    tmp = b
                else:
                    cnt += 1
                    tmp_r.popleft()
                    tmp_r.appendleft(b * 2)
                    tmp = 0
            tmp_r = [0] * cnt + list(tmp_r)
            result.append(tmp_r)
        graph = result
    maximum = 0
    for i in graph:
        maximum = max(maximum, max(i))
    return maximum
    
answer = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    graph_c = copy.deepcopy(graph)
                    answer = max(answer, move([i,j,k,l,m], graph_c))
print(answer)