def main():
    """
    Calculate the minimum number of T-shirts Takahashi needs to buy to meet the conditions.

    Parameters:
    N (int): Number of days.
    M (int): Number of plain T-shirts Takahashi initially has.
    S (str): String representing Takahashi's schedule for N days.

    Returns:
    int: Minimum number of T-shirts Takahashi needs to buy.
    """
    # N日間
    # 長さNの文字列S
    # Mは最初に持っている無地のTシャツの数

    N, M = map(int, input().split())
    S = input()
    logo_tshirts = 0   # Initially, Takahashi has no logo T-shirts
    plain_tshirts = M  # Initially, Takahashi has M plain T-shirts
    plain_used_tshirts = 0
    logo_used_tshirts = 0

    for i in range(N):
        if S[i] == '0':
            plain_used_tshirts = 0
            logo_used_tshirts = 0
        elif S[i] == '1':
            # On days with a meal plan, use a plain T-shirt if available, else use a logo T-shirt
            if plain_tshirts == 0:
                logo_tshirts += 1
                logo_used_tshirts += 1
                # print("elif S[i] == '1': if plain_tshirts == 0:"+str(logo_tshirts))
            elif plain_tshirts > plain_used_tshirts:
                plain_used_tshirts += 1
            elif plain_tshirts == plain_used_tshirts:
                if logo_tshirts > logo_used_tshirts:
                  logo_used_tshirts += 1
                else:
                  logo_tshirts += 1
                  logo_used_tshirts += 1
                # print("elif S[i] == '1': plain_tshirts == plain_used_tshirts:"+str(logo_tshirts))
            else:
                # If no plain T-shirts are available, buy a logo T-shirt if not already bought
                # if used_tshirts == logo_tshirts:
                #     logo_tshirts += 1
                # used_tshirts += 1
                if logo_tshirts > logo_used_tshirts:
                # logo_tshirts += 1
                  logo_used_tshirts += 1
                else:
                  logo_tshirts += 1
                  logo_used_tshirts += 1
                # print("elif S[i] == '1': else"+str(logo_tshirts))
        elif S[i] == '2':
            # On days with a competitive programming event, use a logo T-shirt
            # Buy a logo T-shirt if not already bought
            # if used_tshirts == logo_tshirts:
            #     logo_tshirts += 1
            # used_tshirts += 1
            if logo_tshirts > logo_used_tshirts:
                # logo_tshirts += 1
                logo_used_tshirts += 1
            else:
              logo_tshirts += 1
              logo_used_tshirts += 1
            # print("elif S[i] == '2':"+str(logo_tshirts))

    if (logo_tshirts) <= 0:
        print(0)
    else:
      print(logo_tshirts)


if __name__ == "__main__":
    main()