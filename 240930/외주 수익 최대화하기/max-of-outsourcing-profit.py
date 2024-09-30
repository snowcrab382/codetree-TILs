# input
n = int(input())
works = [list(map(int,input().split())) for i in range(n)]

# solution
dp = [0] * (n + 1)
dp[0] = 0
for i, work in enumerate(works):
    t, p = work[0], work[1]
    if i + t > n:
        continue
    dp[i + t] = max(dp[i + t], max(dp[:i + 1]) + p)
print(max(dp))