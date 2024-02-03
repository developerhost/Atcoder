from collections import deque

def optimized_bfs(grid, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上, 下, 左, 右
    start_positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']
    queue = deque([(start_positions[0], start_positions[1], 0)])  # ((row1, col1), (row2, col2), steps)
    visited = set([(start_positions[0], start_positions[1])])

    while queue:
        (row1, col1), (row2, col2), steps = queue.popleft()

        if (row1, col1) == (row2, col2):
            return steps

        for dr, dc in directions:
            new_pos1 = (row1 + dr, col1 + dc)
            new_pos2 = (row2 + dr, col2 + dc)

            # 移動可能かどうかをチェックし、障害物にぶつかる場合は元の位置に留まる
            if not (0 <= new_pos1[0] < N and 0 <= new_pos1[1] < N and grid[new_pos1[0]][new_pos1[1]] != '#'):
                new_pos1 = (row1, col1)
            if not (0 <= new_pos2[0] < N and 0 <= new_pos2[1] < N and grid[new_pos2[0]][new_pos2[1]] != '#'):
                new_pos2 = (row2, col2)

            if (new_pos1, new_pos2) not in visited:
                visited.add((new_pos1, new_pos2))
                queue.append((new_pos1, new_pos2, steps + 1))

    return -1  # 会えない場合

def main():
    N = int(input().strip())
    grid = [input().strip() for _ in range(N)]
    print(optimized_bfs(grid, N))

if __name__ == "__main__":
    main()