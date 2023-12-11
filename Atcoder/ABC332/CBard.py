def main():
    N, M = map(int, input().split())
    S = input()

    # 食事に行く日の数
    meal_count = S.count("1")

    # 競技プログラミングのイベントに行く日の数
    competition_count = S.count("2")

    # ロゴ入りTシャツを購入する枚数
    required_count = meal_count + competition_count

    # 無地Tシャツを洗濯した回数
    wash_count = 0

    # ロゴ入りTシャツを洗濯した回数
    logo_wash_count = 0

    # 高橋君が着用可能なTシャツの枚数
    available_count = M + wash_count - logo_wash_count

    # 条件を満たすかどうかを判定
    if required_count <= available_count:
        print(required_count - 1)
    else:
        print(0)

if __name__ == "__main__":
    main()
