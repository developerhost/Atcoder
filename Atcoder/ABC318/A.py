# import io
# import sys

# _INPUT = """\
# 13 3 5
# """
# sys.stdin = io.StringIO(_INPUT)

# N M Pを標準入力で取得
N, M, P = map(int, input().split())

ans = 0

# MからNまでP刻みでループ
for i in range(M, N+1, P):
    # ansにiを加算
    ans += 1
    # print(i)

# ansを出力
print(ans)