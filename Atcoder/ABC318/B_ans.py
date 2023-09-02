N = int(input())
painted_area = set() # 矩形が塗られた領域を格納する空のセットを作成

for _ in range(N):
    # a, b, c, dを入力として受け取り、それぞれ左下のx座標、右上のx座標、左下のy座標、右上のy座標とする
    a, b, c, d = map(int, input().split())
    for i in range(a, b): # x座標の範囲でループ
        for j in range(c, d): # y座標の範囲でループ
            painted_area.add((i, j)) # (i, j)の座標を塗られた領域としてセットに追加

s = len(painted_area) # 塗られた領域のセットの要素数を取得し、sに代入
print(s)
# print(painted_area)

