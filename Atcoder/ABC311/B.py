import io
import sys

_INPUT = """\
3 5
xooox
oooxx
oooxo
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

print(H, W)

print("S:----")

for i in range(H):
    print(S[i])

print("----")
print("")

res = 0
length = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            length += 1
            res = max(res, length)
        else:
            res += length*(length+1)//2
            length = 0


# answer = 2