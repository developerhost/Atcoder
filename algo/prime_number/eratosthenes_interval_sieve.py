"""
問題文

2 以上の整数 A,B が与えられます。

A 以上 B 以下の素数が何個あるかを答えてください。
"""

import math

# 入力
A, B = map(int, input().split())

# √B以下の素数を求める
sqrt_B = int(math.sqrt(B) + 0.1) # 0.1を足しているのは、誤差を考慮するため sqrt(9) = 3.0000000000004 などとなるため
is_prime = [True] * (sqrt_B + 1) # Trueのリストを作成 +1しているのは、0から始まるため

# A以上B以下の素数を求める
# その答えは isprime2[v-A] に格納される
is_prime2 = [True] * (B - A + 1)

for i in range(2, sqrt_B + 1):
    # すでに除外されているならばスキップ
    if not is_prime[i]:
        continue
    
    # i の倍数を除外していく
    j = i * 2
    while j * j <= sqrt_B:
        is_prime[j] = False
        j += i

    # A以上の最小のiの倍数を求める
    start = A + (-A) % i
    if start == i:
        start = i * 2

    # iの倍数を除外していく
    j = start
    while j <= B:
        is_prime2[j - A] = False
        j += i

# 答えを数える
print(sum(is_prime2))