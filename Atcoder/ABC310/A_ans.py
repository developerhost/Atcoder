N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

# 選択肢1: 割引券を使わず定価P円で購入
cost_1 = P

# 選択肢2: 割引券を使ってQ円で購入し、追加でN品の中から最も安いものを選ぶ
cost_2 = Q + min(D)

print(min(cost_1, cost_2))
