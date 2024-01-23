def min_operations_to_o_line(H, W, K, grid):
    # def count_dots(grid, i, j, d_i, d_j):
    #     # K 'o の潜在的な行にある '. の数を数えます
    #     return sum(grid[i + d_i * k][j + d_j * k] == '.' for k in range(K))
    def find_min_dots(grid, start_i, start_j, d_i, d_j):
        # 'o' に達する前に連続した '.' の最小数を求める
        min_dots = float('inf')
        dots = 0
        for k in range(K):
            if grid[start_i + d_i * k][start_j + d_j * k] == '.':
                dots += 1
            else:
                # 'o' が見つかったらそれ以降は調べない
                break
        return min_dots if dots < K else 0

    # 最小限の操作を大きな数に初期化します
    min_ops = float('inf')

    # 各行と各列に'x'が存在するかを事前計算し、冗長なチェックを避ける
    row_has_x = ['x' in row for row in grid]
    col_has_x = ['x' in [grid[i][j] for i in range(H)] for j in range(W)]

    # 水平線の各開始点を確認します
    for i in range(H):
        if row_has_x[i]:
            continue  # 行に'x'が含まれている場合はスキップ
        for j in range(W - K + 1):
            if 'x' not in grid[i][j:j+K]:
              print("i:"+str(i)+" j:"+str(j))
              print(find_min_dots(grid, i, j, 0, 1))
              min_ops = min(min_ops, find_min_dots(grid, i, j, 0, 1))

    # 各開始点の縦線を確認する
    for i in range(H - K + 1):
        for j in range(W):
            if col_has_x[j]:
              continue  # 列に'x'が含まれている場合はスキップ
            if 'x' not in grid[i][j:j+K]:
              print("i:"+str(i)+" j:"+str(j))
              print(find_min_dots(grid, i, j, 1, 0))
              min_ops = min(min_ops, find_min_dots(grid, i, j, 1, 0))

    # 有効な行が見つからなかった場合は -1 を返し、それ以外の場合は最小の操作数を返します。
    return -1 if min_ops == float('inf') else min_ops

# test
# 標準入力から入力を読み取る
# H, W, K = map(int, input().split())
# grid = [input().strip() for _ in range(H)]
H, W, K = 10, 12, 6
grid = [
    "......xo.o..",
    "x...x.....o.",
    "x...........",
    "..o...x.....",
    ".....oo.....",
    "o.........x.",
    "ox.oox.xx..x",
    "....o...oox.",
    "..o.....x.x.",
    "...o........",
]



# 答えを計算して出力する
answer = min_operations_to_o_line(H, W, K, grid)
print(answer)