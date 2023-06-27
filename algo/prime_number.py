# 素数かどうか判定する関数

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # 偶数はあらかじめ除く
        return False
    i = 3
    while i * i <= n:  # iがnの平方根を超えるまで
        if n % i == 0: # 割り切れるかどうか
            return False
        i += 2
    return True

N = 1000000007

# 判定
if is_prime(N):
    print('Yes')
else:
    print('No')