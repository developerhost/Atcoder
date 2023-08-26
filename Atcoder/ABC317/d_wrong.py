# テストケースは通ったが、WAになったコード
def solve_election(N, areas):
    # 議席の総数の半分以上を獲得するための閾値を計算
    total_seats = sum([z for _, _, z in areas])
    half_seats = total_seats // 2 + 1

    already_won_seats = sum([z for x, y, z in areas if x > y])
    change_list = []

    for x, y, z in areas:
        if x < y:
            diff = (y - x + 1) // 2
            # ここで効率（議席数/鞍替え人数）を計算
            efficiency = z / diff
            change_list.append((diff, z, efficiency))

    # 効率の降順でソート
    change_list.sort(key=lambda x: (-x[2], x[0]))

    needed_change = 0
    for diff, z, _ in change_list:
        if already_won_seats < half_seats:
            already_won_seats += z
            needed_change += diff
        else:
            break

    return needed_change

# 入力部分
N = int(input())
areas = [tuple(map(int, input().split())) for _ in range(N)]

# 出力部分
print(solve_election(N, areas))
