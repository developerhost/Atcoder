def solve():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 売り手と買い手の価格をソート
    A.sort()
    B.sort()

    # 二分探索を用いて問題を解く
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        X = (l + r) // 2

        # 販売価格Xで売ることを考えている売り手の人数を求める
        sell = sum(i <= X for i in A)

        # 購入価格Xで買うことを考えている買い手の人数を求める
        buy = M - sum(i < X for i in B)

        # 販売価格Xで売ることを考えている売り手の人数が、X円で買うことを考えている買い手の人数以上ならば、
        # Xは可能性のある解なので、探索範囲を[X, r)に更新する。そうでなければ、探索範囲を[l, X)に更新する。
        if sell >= buy:
            r = X
        else:
            l = X

    # rが条件を満たす最小のXになっている
    return r

print(solve())
