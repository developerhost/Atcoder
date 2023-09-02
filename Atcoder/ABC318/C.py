N, D, P = map(int, input().split())
F = list(map(int, input().split()))

# 1. Fiを降順にソート
F.sort(reverse=True)

total_cost = 0
i = 0

# 2. 1日周遊パスが使えるかどうかを調べるループ
while i < N:
    # 3. Fiの上からD個取得した合計とPを比較
    if sum(F[i:i+D]) > P:
        total_cost += P
        i += D
    else:
        total_cost += F[i]
        i += 1

# 5. 合計コストを出力
print(total_cost)
