from collections import deque

def optimized_bfs(grid, N):
  """
  2人のプレイヤーが同じ連結成分にいるかどうかを判定し、
  同じ連結成分にいる場合はその距離、
  そうでない場合は-1を返す

  Args:
    grid: マップを表すN×Nの文字列リスト
    N: マップのサイズ

  Returns:
    2人のプレイヤーの距離、または-1
  """

  # 移動方向
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 上, 下, 左, 右

  # プレイヤーの初期位置
  player_positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']

  # 開始位置
  start_positions = tuple(player_positions)

  # 訪問済み集合
  visited = set([start_positions])

  # キュー
  queue = deque([(start_positions, 0)]) # ((row1, col1), (row2, col2), steps)

  # 有効な位置かどうかを判定する関数
  def is_valid_position(pos):
    row, col = pos
    return 0 <= row < N and 0 <= col < N and grid[row][col] != '#'

  # 探索ループ
  while queue:
    (row1, col1), (row2, col2), steps = queue.popleft()

    # 2人のプレイヤーが同じ位置にいる場合
    if (row1, col1) == (row2, col2):
      return steps

    # 4方向に移動
    for dr, dc in directions:
      new_pos1 = (row1 + dr, col1 + dc)
      new_pos2 = (row2 + dr, col2 + dc)

      # 壁にぶつかった場合は移動しない
      if not is_valid_position(new_pos1):
        new_pos1 = (row1, col1)
      if not is_valid_position(new_pos2):
        new_pos2 = (row2, col2)

      # 新しい位置が訪問済みでない場合
      new_positions = (new_pos1, new_pos2)
      if new_positions not in visited:
        visited.add(new_positions)
        queue.append((new_positions, steps + 1))

  # 2人のプレイヤーが同じ連結成分にいない場合
  return -1

def main():
  """
  メイン関数
  """

  # マップのサイズ
  N = int(input().strip())

  # マップ
  grid = [input().strip() for _ in range(N)]

  # 2人のプレイヤーの距離を出力
  print(optimized_bfs(grid, N))

if __name__ == "__main__":
  main()
