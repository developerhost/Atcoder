import sys
from operator import itemgetter
import io

_INPUT = """\
4
0 0 0 1 1 1
0 0 1 1 1 2
1 1 1 2 2 2
3 3 3 4 4 4
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input().strip())
events = [[] for _ in range(3)]
for i in range(N):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    # Add events for x dimension
    events[0].append((x1, i, 1))
    events[0].append((x2, i, -1))
    # Add events for y dimension
    events[1].append((y1, i, 1))
    events[1].append((y2, i, -1))
    # Add events for z dimension
    events[2].append((z1, i, 1))
    events[2].append((z2, i, -1))

for e in events:
    e.sort()

cnt = [0] * N
cnt_d = [[0] * N for _ in range(3)]
S_d = [set() for _ in range(3)]
for d in range(3):
    S = set()
    for _, i, e in events[d]:
        if e == 1:
            cnt[i] += len(S) - cnt_d[d][i]
            S.add(i)
        else:
            S.remove(i)
            cnt[i] -= len(S)
            cnt_d[d][i] = len(S)
for c in cnt:
    print(c)
