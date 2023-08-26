# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# N個の整数の和
sum_N = sum(A)

# 本来の和を計算
min_val = min(A)
max_val = max(A)

# 連続する整数の和の公式: n*(n+1)/2 を利用
sum_Nplus1 = (max_val * (max_val + 1) - (min_val - 1) * min_val) // 2

# 結果を出力
print(sum_Nplus1 - sum_N)
