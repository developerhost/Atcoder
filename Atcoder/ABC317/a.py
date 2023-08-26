# 入力
N, H, X = map(int, input().split())
P = list(map(int, input().split()))

# 目標体力X以上になる最も効果が弱い薬を探す
for i in range(N):
    if H + P[i] >= X:
        print(i+1)
        break
