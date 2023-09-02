import bisect, heapq, sys, math, copy, itertools
from collections import defaultdict, deque
import io

sys.setrecursionlimit(10**8)
def INT(): return int(input())
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def LI(): return list(map(int, input().split()))
def LS(): return list(map(str, input().split()))
def pr_line(itr): print(*itr, sep='\n')
def pr_mtx(matrix): [print(*row) for row in matrix] 
INF = 1<<62

_INPUT = """\
4
1 5 4
7 8
6
"""
sys.stdin = io.StringIO(_INPUT)



N = INT()
D = [LI() for _ in range(N-1)]

print("D")
print(D)
print("")

dp = [0 for _ in range(1<<N)]

for bit in range(1<<N): # 0から2^N-1までの範囲でbitという変数が増加します
    # 各ループ内で、2重のループを実行します。これらのループは、すべての頂点の組み合わせに対して繰り返されます。
    for i in range(N-1): # 0からN-2までの範囲でiという変数が増加
        for j in range(i+1, N): # i+1からN-1までの範囲でjという変数が増加
            if (bit>>i) & 1 == 0 and (bit>>j) & 1 == 0: # もしbitのiビット目とjビット目がともに0であれば（つまり、i番目とj番目の頂点が選択されていない場合）、nxtという変数を計算します。
                nxt = (bit | (1<<i)) | (1<<j) # dp[nxt]の値を更新します。具体的には、dp[bit] + D[i][j-i-1]の値とdp[nxt]の値を比較し、より大きい方をdp[nxt]に代入します
                print("bit", bit)
                print("i", i)
                print("j", j)
                print("nxt", nxt)
                dp[nxt] = max(dp[nxt], dp[bit] + D[i][j-i-1])
                print("dp[nxt]", dp[nxt])

print(dp[-1])