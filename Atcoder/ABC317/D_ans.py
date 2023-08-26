from sys import stdin
input = stdin.readline
inf = 1 << 60

n = int(input())
x = [0] * n
y = [0] * n
z = [0] * n
for i in range(n):
    x[i], y[i], z[i] = map(int, input().split())

sum_z = sum(z) // 2 + 1

dp = [inf] * (sum_z + 1)
dp[0] = 0
for i in range(n):
    cost = 0 if x[i] > y[i] else (y[i] - x[i]) // 2 + 1
    for j in reversed(range(sum_z)):
        dp[min(sum_z, j + z[i])] = min(dp[min(sum_z, j + z[i])], dp[j] + cost)

print(dp[sum_z])
