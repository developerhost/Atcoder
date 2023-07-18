# 双子素数を数える問題

"""
出力例 3
10
(3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73), (101,103), (107,109) の 10 組です。
"""

# 1以上N以下の整数が素数かどうかを返す 素数がTrue
def Eratosthenes(N):
    # テーブル
    is_prime = [True] * (N + 1)
    
    # 0, 1は予め除外しておく
    is_prime[0] = False
    is_prime[1] = False

    # 素数でないものを除外していく
    for i in range(2, N + 1):
        # すでに除外されているならばスキップ
        if not is_prime[i]: # is_prime[i] == False と同じ
            continue
        
        # i の倍数を除外していく
        j = i * 2 # jがi * 2から始まるのは、i * 2 以前はすでに除外されているから
        while j <= N:
            is_prime[j] = False
            j += i

    return is_prime

# 入力
N = int(input())

# エラトステネスの篩
is_prime = Eratosthenes(N)

# 結果
count = 0
for i in range(2, N - 1):
    if is_prime[i] and is_prime[i + 2]:
        count += 1

print(count)