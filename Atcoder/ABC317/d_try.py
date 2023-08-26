# TLEする
import itertools

def solve_election(N, areas):
    total_seats = sum([z for _, _, z in areas])
    half_seats = total_seats // 2 + 1

    already_won_seats = sum([z for x, y, z in areas if x > y])

    # 既に半数以上の議席を獲得している場合
    if already_won_seats >= half_seats:
        return 0
    
    to_be_changed_list = []

    for x, y, z in areas:
        if x < y:
            diff = (y - x + 1) // 2
            to_be_changed_list.append((diff, z))

    # 議席が過半数を超える最小の鞍替え人数を求める
    min_changes = float('inf')
    for L in range(1, len(to_be_changed_list) + 1):
        for subset in itertools.combinations(to_be_changed_list, L):
            total_changes = sum(item[0] for item in subset)
            total_subset_seats = sum(item[1] for item in subset)
            if total_subset_seats + already_won_seats >= half_seats:
                min_changes = min(min_changes, total_changes)

    return min_changes

# 入力部分
N = int(input())
areas = [tuple(map(int, input().split())) for _ in range(N)]

# 出力部分
print(solve_election(N, areas))
