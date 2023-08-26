MOD = 998244353
S = input().strip()  # 入力された文字列を取得し、前後の空白を削除します
N = len(S)  # 文字列の長さを取得します
dp = [[0]*(N+1) for _ in range(N+1)]  # dpテーブルを初期化します
dp[0][0] = 1  # 初期条件として、dp[0][0]を1に設定します

for i in range(N):  # 文字列の各文字についてループします
    for j in range(N+1):  # jは開き括弧の数を表します
        if S[i] != ')':  # もし現在の文字が')'でなければ
            if j < N:  # 開き括弧の数がN未満であれば
                dp[i+1][j+1] += dp[i][j]  # dp[i+1][j+1]にdp[i][j]を加算します
                dp[i+1][j+1] %= MOD  # MODで割った余りを取ります
        if S[i] != '(':  # もし現在の文字が'('でなければ
            if j > 0:  # 開き括弧の数が0より大きければ
                dp[i+1][j-1] += dp[i][j]  # dp[i+1][j-1]にdp[i][j]を加算します
                dp[i+1][j-1] %= MOD  # MODで割った余りを取ります

print(dp[N][0])  # dp[N][0]を出力します
