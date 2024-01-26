# 素因数分解
# 460 = 2^2 x 5 x 23 の場合
# 返り値は [(2, 2), (5, 1), (23, 1)]
def prime_factorize(N):
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append((p, e))
    if N != 1:
        res.append((N, 1))
    return res

# 入力
N = int(input())

# 素因数分解
pf = prime_factorize(N)

# メビウス関数
res = 1
for (p, e) in pf:
    if e > 1:
        res = 0
    else:
        res *= -1
print(res)