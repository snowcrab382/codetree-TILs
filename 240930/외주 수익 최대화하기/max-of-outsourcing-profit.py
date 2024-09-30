# input
n = int(input())
works = [list(map(int,input().split())) for i in range(n)]

# solution
dp = [0] * (n + 1)
dp[0] = 0
for i in range(len(works)):
    t, p = works[i][0], works[i][1]
    if i + t > n:
        continue
    dp[i + t] = max(dp[i + t], max(dp[:i + 1]) + p)
print(max(dp))