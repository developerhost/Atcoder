# ゴールドバッハ予測

"""
4 以上の偶数 N が与えられます。 N を 2 つの素数の和として表してください。
より具体的には、N=p+q と表せるような 2 つの素数 p,q を求めて、p の値を出力してください。
ただし、そのような p が複数通り考えられる場合には、そのうち最小の値を出力してください。
また、そのような p が存在しない場合には -1 と出力してください。
"""

# 解法

"""
p が素数である
N - p が素数である (q = N - p とすればよい)
という条件を最初に満たす瞬間を捉える
"""

# 素数判定関数

"""
例えば、N = 10 とすると、
def is_prime(n):の中身は以下のようになる
i = 2の場合、i * i <= n は 4 <= 10 となり、True
if n % i == 0 は 10 % 2 == 0 となり、True
i += 1 は i = 3
i = 3の場合、i * i <= n は 9 <= 10 となり、True
if n % i == 0 は 10 % 3 == 0 となり、False

i * iがnを超えるまで（つまりiがsqrt(n)を超えるまで）にnを割り切る整数（n自身と1以外の約数）が見つからなければ、
nは素数と判断され、その値nが返されます。
"""

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n

# 入力
N = int(input())

# N以下の素数を求める
result = -1

# range(2, N + 1) で 2 から N までの整数を順に取り出す
for p in range(2, N + 1):
    if is_prime(p) and is_prime(N - p): # p が素数かつ N - p も素数ならば
        result = p
        break
    
print(result)