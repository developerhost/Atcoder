# 長さの違う線を使って10cmを作れるのか。DPで解く。

N = 5
length = 10
lines = [4, 7, 8, 5, 1]
 
# dp[i][j] := i本目までの線を使って長さjの線を作れるかどうか
dp = [[False for i in range(length+1)] for j in range(N+1)] # 中身は6*11のFalseの2次元配列

# 初期条件
dp[0][0] = True

# for i in dp:
#     print(i)
# header = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# [True, False, False, False, False, False, False, False, False, False, False]
# [False, False, False, False, False, False, False, False, False, False, False]
# [False, False, False, False, False, False, False, False, False, False, False]
# [False, False, False, False, False, False, False, False, False, False, False]
# [False, False, False, False, False, False, False, False, False, False, False]
# [False, False, False, False, False, False, False, False, False, False, False]

# 順番に線を見てTrueを埋めていく
for i in range(N): # 0, 1, 2, 3, 4 ここは線の本数
    for j in range(length+1): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ここは長さcm
        if dp[i][j]:
            dp[i+1][j] = True # 線は追加されるだけなので、次の線を見るときは既存のTrueはそのままTrue
            if j + lines[i] <= length: # 既存の線に新しい線を追加したときに長さがlengthを超えないか
                dp[i+1][j+lines[i]] = True # [j+lines[i]]は新しい線を追加したときの長さ

for i in dp:
    print(i)
print("--------------------")

# [True, False, False, False, False, False, False, False, False, False, False]
# [True, False, False, False, True, False, False, False, False, False, False]
# [True, False, False, False, True, False, False, True, False, False, False]
# [True, False, False, False, True, False, False, True, True, False, False]
# [True, False, False, False, True, True, False, True, True, True, False]
# [True, True, False, False, True, True, True, True, True, True, True]
# --------------------

print(dp[N][length]) # 10cmを作れるかどうか