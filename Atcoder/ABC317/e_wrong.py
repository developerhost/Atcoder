# テストは通ったが、WAになったコード
from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

# 人の視線を考慮して通行不可のセルを "#" とする
for i in range(H):
    for j in range(W):
        if A[i][j] == '>':
            # ここが間違っていた
            for k in range(j + 1, W):
                if A[i][k] == '.':
                    A[i][k] = '#'
                elif A[i][k] == '#' or A[i][k] in "><^v":
                    break
        elif A[i][j] == '<':
            for k in range(j - 1, -1, -1):
                if A[i][k] == '.':
                    A[i][k] = '#'
                elif A[i][k] == '#' or A[i][k] in "><^v":
                    break
        elif A[i][j] == 'v':
            for k in range(i + 1, H):
                if A[k][j] == '.':
                    A[k][j] = '#'
                elif A[k][j] == '#' or A[k][j] in "><^v":
                    break
        elif A[i][j] == '^':
            for k in range(i - 1, -1, -1):
                if A[k][j] == '.':
                    A[k][j] = '#'
                elif A[k][j] == '#' or A[k][j] in "><^v":
                    break

# dx, dyは上下左右の移動を表す
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
visited = [[False] * W for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            queue.append((i, j, 0))
            visited[i][j] = True

while queue:
    # x, yは現在地、dは現在地までの距離 xは行=H、yは列=W
    x, y, d = queue.popleft()
    if A[x][y] == 'G':
        print(d)
        exit()

    for direction in range(4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and A[nx][ny] not in "#><^v":
            visited[nx][ny] = True
            queue.append((nx, ny, d + 1))

print(-1)
