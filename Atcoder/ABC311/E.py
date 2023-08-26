import io
import sys

_INPUT = """\
2 3 1
2 3
"""
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
S = [[0]*W for _ in range(H)]

print("S:----")

for i in range(H):
    print(S[i])

print("----")
print("")

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    S[a][b] = 1

print("S_ab:----")

for i in range(H):
    print(S[i])

print("----")
print("")

# dp[i+1][j+1] := マス (i, j) を右下マスとする最大の正方形の一辺の長さ
dp = [[0]*(W+1) for _ in range(H+1)]

print("dp:----")
for i in range(H+1):
    print(dp[i])
print("----")

for i in range(H):
    for j in range(W):
        if S[i][j] == 0:
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1

print("dp_ij:----")
for i in range(H+1):
    print(dp[i])
print("----")

# 集計
res = 0
for i in range(H):
    for j in range(W):
        res += dp[i+1][j+1]
print(res)
