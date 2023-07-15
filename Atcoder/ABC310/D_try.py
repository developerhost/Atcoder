"""
問題文
```
N 人のスポーツ選手がいます。

N 人の選手たちには互いに相性の悪い選手のペアがM 組あり、相性の悪い組のうちi(1≤i≤M) 組目はAi番目の選手とBi番目の選手です。

あなたは、選手をTチームに分けます。 どの選手もちょうど一つのチームに属さなければならず、どのチームにも少なくとも一人の選手が属さなければなりません。 
さらに、どのi=1,2,…,M についても、Ai番目の選手とBi番目の選手が同じチームに属していてはいけません。
この条件を満たすチーム分けの方法は何通りあるか求めてください。 ただし、チーム分けの方法が異なるとは、ある二人が存在して、彼らが一方のチーム分けでは同じチームに所属し、もう一方では異なるチームに所属することをいいます。
```

制約
```
・1≤T≤N≤10
・0≤M≤N(N−1)/2
・1≤Ai<Bi≤N (1≤i≤M)
・(Ai,Bi)!=(Aj,Bj) (1≤i<j≤M)
・入力はすべて整数
```

入力
入力は以下の形式で標準入力から与えられる。
```
N T M
A1 B1
A2 B2
​⋮
AM BM
 ```
出力
```
答えを1行で出力せよ。
```

入力例 1 
```
5 2 2
1 3
3 4
```

出力例 1 
```
4
```
"""

from operator import mul
from functools import reduce
from collections import deque
from itertools import combinations

import io
import sys

_INPUT = """\
5 2 2
1 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)

N, T, M = map(int, input().split())
pairs = []

for _ in range(M):
    A, B = map(int, input().split())
    pairs.append((A, B))

print(pairs)

# def solve(N, T, M, pairs):
#     # 1. Find all possible combinations of T teams from N players
#     # 2. For each combination, check if it satisfies the condition
#     # 3. Count the number of combinations that satisfy the condition
#     # 4. Return the count
#     count = 0
#     for comb in combinations(range(N), T):
#         print(comb)
#         print([p for p in pairs if p[0] in comb and p[1] in comb])
#         if len([p for p in pairs if p[0] in comb and p[1] in comb]) == 0:
#             count += 1
#     return count

# def main():
#     N, T, M = map(int, input().split())
#     pairs = []
#     for _ in range(M):
#         A, B = map(int, input().split())
#         pairs.append((A-1, B-1))
#     print(solve(N, T, M, pairs))

# if __name__ == "__main__":
#     main()