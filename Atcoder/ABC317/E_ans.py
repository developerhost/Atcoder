from collections import deque
import sys
input = sys.stdin.readline

# Hは行数、Wは列数
H, W = map(int, input().split())

# Aは迷路の情報を格納する2次元配列
A = [input().rstrip() for _ in range(H)]

# sightは人の視線を考慮した通行不可のセルを格納する2次元配列
sight = [[0]*W for _ in range(H)]

for i in range(H):
    s = 0
    for j in range(W):
        if A[i][j] == '>':
            s = 1
        elif A[i][j] != '.':
            s = 0
        sight[i][j] |= s
    for j in range(W)[::-1]:
        if A[i][j] == '<':
            s = 1
        elif A[i][j] != '.':
            s = 0
        sight[i][j] |= s
for j in range(W):
    s = 0
    for i in range(H):
        if A[i][j] == 'v':
            s = 1
        elif A[i][j] != '.':
            s = 0
        sight[i][j] |= s
    for i in range(H)[::-1]:
        if A[i][j] == '^':
            s = 1
        elif A[i][j] != '.':
            s = 0
        sight[i][j] |= s


dist = [[-1] * W for _ in range(H)]
que = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            dist[i][j] = 0
            que.append((i, j))
while que:
    i, j = que.popleft()
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i+di, j+dj
        # ni, njが迷路の範囲内で、通行可能で、未探索の場合
        if 0 <= ni < H and 0 <= nj < W and A[ni][nj] != '#' and not sight[ni][nj] and dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j] + 1
            que.append((ni, nj))
for i in range(H):
    for j in range(W):
        if A[i][j] == 'G':
            print(dist[i][j])
