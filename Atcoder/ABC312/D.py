MOD = 998244353
S = input().strip()
N = len(S)
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(N+1):
        if S[i] != ')':
            if j < N:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
        if S[i] != '(':
            if j > 0:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= MOD

print(dp[N][0])
