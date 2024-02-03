import sys
from collections import deque

def bfs_simultaneous_moves(grid, N):
    if can_meet(grid, N) == False:
        return -1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上, 下, 左, 右
    player_positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']

    if len(player_positions) != 2:
        return -1

    start = (player_positions[0], player_positions[1], 0)  # ((row1, col1), (row2, col2), steps)
    queue = deque([start])
    visited = set([start])


    while queue:
        (row1, col1), (row2, col2), steps = queue.popleft()

        # 2人のプレイヤーが同じマスに到達した場合
        if (row1, col1) == (row2, col2):
            return steps

        for dr, dc in directions:
            new_row1, new_col1 = row1 + dr, col1 + dc
            new_row2, new_col2 = row2 + dr, col2 + dc

            # 移動可能かどうかをチェックし、障害物にぶつかる場合は元の位置に留まる
            if not (0 <= new_row1 < N and 0 <= new_col1 < N and grid[new_row1][new_col1] != '#'):
                new_row1, new_col1 = row1, col1  # プレイヤー1は移動しない

            if not (0 <= new_row2 < N and 0 <= new_col2 < N and grid[new_row2][new_col2] != '#'):
                new_row2, new_col2 = row2, col2  # プレイヤー2は移動しない

            new_state = ((new_row1, new_col1), (new_row2, new_col2), steps + 1)

            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    return -1  # 2人のプレイヤーが会合できない場合

def is_same_component(grid, N, start, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上, 下, 左, 右
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col] and grid[new_row][new_col] != '#':
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))

def can_meet(grid, N):
    visited = [[False] * N for _ in range(N)]
    player_positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']

    # 最初のプレイヤーから探索を開始して、訪問した全ての空きマスをマーク
    is_same_component(grid, N, player_positions[0], visited)

    # 二人目のプレイヤーが最初のプレイヤーと同じ連結成分に属しているかどうかをチェック
    second_player_pos = player_positions[1]
    if visited[second_player_pos[0]][second_player_pos[1]]:
        return True  # 二人のプレイヤーは同じ連結成分に属している（会える）
    else:
        return False  # 二人のプレイヤーは異なる連結成分に属している（会えない）

def main():
    N = int(input().strip())
    grid = [input().strip() for _ in range(N)]
    print(bfs_simultaneous_moves(grid, N))

if __name__ == "__main__":
    main()
