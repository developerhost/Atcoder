def calculate_tshirts_needed(N, M, S):
    # 最初に持っている無地のTシャツの数
    plain_tshirts = M
    # 購入する必要のあるロゴ入りTシャツの数
    logo_tshirts_needed = 0

    for day in range(N):
        if S[day] == '1':
            # 食事の予定がある日: 無地またはロゴ入りTシャツを1枚着用
            if plain_tshirts > 0:
                # 無地のTシャツがあればそれを使用
                plain_tshirts -= 1
            else:
                # 無地のTシャツがなければロゴ入りを使用 (必要に応じて購入)
                logo_tshirts_needed += 1
        elif S[day] == '2':
            # 競技プログラミングのイベントの日: ロゴ入りTシャツを1枚着用
            logo_tshirts_needed += 1
        elif S[day] == '0':
            # 予定がない日: すべてのTシャツを洗濯
            plain_tshirts = M + logo_tshirts_needed  # 洗濯済みとなるTシャツの総数

    return logo_tshirts_needed

# テストケースを実行
print(calculate_tshirts_needed(6, 1, "112022"))  # 出力例1
print(calculate_tshirts_needed(3, 1, "222"))     # 出力例2
print(calculate_tshirts_needed(2, 1, "01"))      # 出力例3