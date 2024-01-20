def min_operations(H, W, K, grid):
  """
  特定の条件を達成するために必要な操作の最小数を計算します。

  args：
    H（int）：グリッドの高さ。
    W（int）：グリッドの幅。
    K（int）：各行または列に必要な連続した「x」の数。
    grid（list [list [str]]）： 'x' and '。を含むグリッド。

  戻り値：
    INT：必要な操作の最小数。状態を達成することが不可能な場合は-1を返します。
  """
  min_ops = float('inf')

  # 各行と列に 'x' と '.' の数を事前計算する
  count_x_row = [[0]*(W+1) for _ in range(H)]
  count_dot_row = [[0]*(W+1) for _ in range(H)]
  count_x_col = [[0]*(H+1) for _ in range(W)]
  count_dot_col = [[0]*(H+1) for _ in range(W)]

  for i in range(H):
    for j in range(W):
      # count_x_rowは、i行目のj列目までのxの数を格納する
      count_x_row[i][j+1] = count_x_row[i][j] + (grid[i][j] == 'x')
      # count_dot_rowは、i行目のj列目までの連続した.の数を格納する
      count_dot_row[i][j+1] = count_dot_row[i][j] + (grid[i][j] == '.')
  for j in range(W):
    for i in range(H):
      # count_x_colは、j列目のi行目までのxの数を格納する
      count_x_col[j][i+1] = count_x_col[j][i] + (grid[i][j] == 'x')
      # count_dot_colは、j列目のi行目までの連続した.の数を格納する
      count_dot_col[j][i+1] = count_dot_col[j][i] + (grid[i][j] == '.')

  # 各行が条件を満たすかどうかを確認する
  for i in range(H):
    for j in range(W-K+1):
      # ifは、i行目のj列目からj+K-1列目までにxが含まれていないかどうかを確認する
      if count_x_row[i][j+K] - count_x_row[i][j] == 0:
        # opsは、i行目のj列目からj+K-1列目までに連続した.が含まれている数を格納する
        ops = count_dot_row[i][j+K] - count_dot_row[i][j]
        print("i:"+str(i)+" j:"+str(j)+" ops:"+str(ops))
        min_ops = min(min_ops, ops)

  # 各列が条件を満たすかどうかを確認する
  for j in range(W):
    for i in range(H-K+1):
      # ifは、j列目のi行目からi+K-1行目までにxが含まれていないかどうかを確認する
      if count_x_col[j][i+K] - count_x_col[j][i] == 0:
        # opsは、j列目のi行目からi+K-1行目までに.が含まれている数を格納する
        ops = count_dot_col[j][i+K] - count_dot_col[j][i]
        min_ops = min(min_ops, ops)

  return min_ops if min_ops != float('inf') else -1

def main():
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
    print(min_operations(H, W, K, grid))

if __name__ == "__main__":
    main()