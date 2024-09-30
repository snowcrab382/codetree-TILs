# input
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# solution
arr = [i for i in range(n)]
half = n // 2

def check(arr_a, arr_b):
    cal_a, cal_b = 0, 0
    for i in arr_a:
        for j in arr_a:
            cal_a += graph[i][j]
    
    for i in arr_b:
        for j in arr_b:
            cal_b += graph[i][j]

    return abs(cal_a - cal_b)

def combinations(half, new_arr, c):
    global result

    if len(new_arr) == half:
        remain_arr = []
        for i in range(n):
            if i not in new_arr:
                remain_arr.append(i)
        result = min(result, check(new_arr, remain_arr))
        return
    
    for i in range(c, len(arr)):
        combinations(half, new_arr + [arr[i]], i + 1)

result = 9999999999
combinations(half, [], 0)
print(result)