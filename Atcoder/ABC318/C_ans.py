N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
i = 0
ans = 0
# range(0, N, D) を使って、0 から N まで D 刻みでループします。
for i in range(0, N, D):
    # F[i:i+D] の要素の合計と P の小さい方を選んで、ans に加算します。
    ans += min(sum(F[i:i+D]), P)
# print(i)
print(ans)
