import math
from collections import defaultdict
#test : oj t -c 'python3 abc310/b/main.py' -d abc310/b/tests/
#submit : cd abc310/b && acc s

N, M = map(int, input().split())
P, C, F = [], [], []
for _ in range(N):
    l = list(map(int, input().split()))
    P.append(l[0])
    C.append(l[1])
    F.append(set(l[2:]))
ans = False
for i in range(N):
    for j in range(N):
        # P[i] >= P[j]
        # F[j].issuperset(F[i])：j番目の要素F[j]がi番目の要素F[i]を包含していることを確認します。
        # (P[i] > P[j] or len(F[j]) > len(F[i]))：i番目の要素P[i]がj番目の要素P[j]よりも大きいか、
        # またはi番目の要素F[i]の長さがj番目の要素F[j]の長さよりも大きいことを確認します。
        ans |= P[i] >= P[j] and F[j].issuperset(F[i]) \
            and (P[i] > P[j] or len(F[j]) > len(F[i]))
print('Yes' if ans else 'No')
