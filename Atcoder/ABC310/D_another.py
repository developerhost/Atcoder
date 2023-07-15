from math import factorial as fact

MOD = 10**9 + 7

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact(n) // (fact(r) * fact(n - r))

N, T, M = map(int, input().split())
pairs = [0]*N
dp = [[[[0 for _ in range(T+1)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    pairs[b-1] = a

dp[0][0][0][0] = 1
for i in range(N):
    for j in range(i+1):
        for k in range(i-j+1):
            for t in range(min(T, i+1)):
                if pairs[i] > 0:
                    if pairs[i] <= j:
                        dp[i+1][j][k+1][t] += dp[i][j][k][t] * comb(j, pairs[i] - 1)
                        dp[i+1][j][k+1][t] %= MOD
                        dp[i+1][j+1][k][t] += dp[i][j][k][t] * (comb(j+1, pairs[i]) - comb(j, pairs[i] - 1))
                        dp[i+1][j+1][k][t] %= MOD
                    else:
                        dp[i+1][j+1][k][t] += dp[i][j][k][t] * comb(j+1, pairs[i] - 1)
                        dp[i+1][j+1][k][t] %= MOD
                else:
                    dp[i+1][j+1][k][t] += dp[i][j][k][t]
                    dp[i+1][j+1][k][t] %= MOD
                    if t < T:
                        dp[i+1][j+1][k][t+1] += dp[i][j][k][t] * t
                        dp[i+1][j+1][k][t+1] %= MOD
                    if k > 0:
                        dp[i+1][j][k][t] += dp[i][j][k][t] * k
                        dp[i+1][j][k][t] %= MOD

ans = 0
for j in range(N+1):
    for k in range(N-j+1):
        for t in range(T+1):
            ans += dp[N][j][k][t]
            ans %= MOD

print(ans)
