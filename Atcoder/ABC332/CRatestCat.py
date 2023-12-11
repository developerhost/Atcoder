def min_tshirts_to_buy():
    """
    Calculate the minimum number of T-shirts (both plain and logo) Takahashi needs in total to meet the conditions.

    Parameters:
    N (int): Number of days.
    M (int): Number of plain T-shirts Takahashi initially has.
    S (str): String representing Takahashi's schedule for N days.

    Returns:
    int: Minimum total number of T-shirts (both plain and logo) Takahashi needs.
    """
    N, M = map(int, input().split())
    S = input()
    plain_tshirts = M  # Initially, Takahashi has M plain T-shirts
    logo_tshirts = 0   # Initially, Takahashi has no logo T-shirts
    used_tshirts = 0   # Number of used T-shirts

    for i in range(N):
        if S[i] == '0':
            # On days with no plans, wash all used T-shirts
            plain_tshirts += used_tshirts
            used_tshirts = 0
        elif S[i] == '1':
            # On days with a meal plan, use a plain T-shirt if available, else use a logo T-shirt
            if plain_tshirts > 0:
                plain_tshirts -= 1
                used_tshirts += 1
            else:
                # If no plain T-shirts are available, buy a logo T-shirt if not already bought
                if used_tshirts == logo_tshirts:
                    logo_tshirts += 1
                used_tshirts += 1
        elif S[i] == '2':
            # On days with a competitive programming event, use a logo T-shirt
            # Buy a logo T-shirt if not already bought
            if used_tshirts == logo_tshirts:
                logo_tshirts += 1
            used_tshirts += 1

    # Return the total number of T-shirts (both plain and logo) needed
    if (plain_tshirts + logo_tshirts -1) < 0:
        print(0)
    else:
      print(max(plain_tshirts - 1, logo_tshirts))

min_tshirts_to_buy()