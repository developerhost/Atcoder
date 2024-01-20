def min_operations_to_o_line(H, W, K, grid):
    def check_line(grid, i, j, d_i, d_j):
        # (i, j) から始まる (d_i, d_j) 方向の K'o の列が形成できるかどうかを確認する
        return all(grid[i + d_i * k][j + d_j * k] != 'x' for k in range(K))

    def count_dots(grid, i, j, d_i, d_j):
        # K 'o の潜在的な行にある '. の数を数えます
        return sum(grid[i + d_i * k][j + d_j * k] == '.' for k in range(K))

    # 最小限の操作を大きな数に初期化します
    min_ops = float('inf')

    # 水平線の各開始点を確認します
    for i in range(H):
        for j in range(W - K + 1):
            if check_line(grid, i, j, 0, 1):
                min_ops = min(min_ops, count_dots(grid, i, j, 0, 1))

    # 各開始点の縦線を確認する
    for i in range(H - K + 1):
        for j in range(W):
            if check_line(grid, i, j, 1, 0):
                min_ops = min(min_ops, count_dots(grid, i, j, 1, 0))

    # 有効な行が見つからなかった場合は -1 を返し、それ以外の場合は最小の操作数を返します。
    return -1 if min_ops == float('inf') else min_ops


# 標準入力から入力を読み取る
H, W, K = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 答えを計算して出力する
answer = min_operations_to_o_line(H, W, K, grid)
print(answer)