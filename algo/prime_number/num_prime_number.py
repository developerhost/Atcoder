# N以下の素数の個数を求める

# 素数判定関数
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n

# 1以上N以下の整数が素数かどうかを返す
def Eratosthenes(N):
    # テーブル
    is_prime = [True] * (N + 1)

    # 0, 1 は素数ではない
    is_prime[0] = False
    is_prime[1] = False

    # 素数でないものを除外していく
    for i in range(2, N + 1):
        # すでに除外されているならばスキップ
        if not is_prime[i]:
            continue
        
        # i の倍数を除外していく
        j = i * 2
        while j <= N:
            is_prime[j] = False
            j += i

# 入力
N = int(input())

# エラトステネスの篩
is_prime = Eratosthenes(N)

# 結果
print(sum(is_prime))