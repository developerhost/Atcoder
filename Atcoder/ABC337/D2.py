def min_operations_to_o_line_improved(H, W, K, grid):
    def count_dots_for_line(start_i, start_j, d_i, d_j):
        # Count the number of '.'s in a potential line of K 'o's
        return sum(grid[start_i + d_i * k][start_j + d_j * k] == '.' for k in range(K))

    # 冗長チェックを避けるために、各行と列に「x」の存在を事前に計算します
    row_has_x = ['x' in row for row in grid]
    col_has_x = ['x' in [grid[i][j] for i in range(H)] for j in range(W)]

    min_ops = float('inf')

    # 水平線の各出発点を確認します
    for i in range(H):
        if row_has_x[i]:
            continue  # Skip the row if it contains 'x'
        for j in range(W - K + 1):
            if not any(col_has_x[j + k] for k in range(K)):  # Check if any column in the range has 'x'
                min_ops = min(min_ops, count_dots_for_line(i, j, 0, 1))

    # Check each starting point for vertical lines
    for j in range(W):
        if col_has_x[j]:
            continue  # Skip the column if it contains 'x'
        for i in range(H - K + 1):
            if not any(row_has_x[i + k] for k in range(K)):  # Check if any row in the range has 'x'
                min_ops = min(min_ops, count_dots_for_line(i, j, 1, 0))

    return -1 if min_ops == float('inf') else min_ops

# Read input from standard input
H, W, K = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Calculate and output the answer
answer = min_operations_to_o_line_improved(H, W, K, grid)
print(answer)
