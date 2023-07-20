# 入力
N = int(input())

# √N まで試す
res = N+1  # (N, 1) の組がとりあえずある
for A in range(1, N + 1):
    # √N で打ち切ってよい
    if A * A > N:
        break
    
    # 約数でない場合はスキップ
    if N % A != 0:
        continue

    # より小さいなら更新
    res = min(res, A + N//A)

print(res)