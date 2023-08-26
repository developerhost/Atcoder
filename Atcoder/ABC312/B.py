import io
import sys

_INPUT = """\
19 18
###......###......
###......###......
###..#...###..#...
..............#...
..................
..................
......###......###
......###......###
......###......###
.###..............
.###......##......
.###..............
............###...
...##.......###...
...##.......###...
.......###........
.......###........
.......###........
........#.........
"""
sys.stdin = io.StringIO(_INPUT)

def is_tak_code(grid):
    for i in range(9): # i: 行 j: 列
        for j in range(9):
            if (i < 3 and j < 3) or (i >= 6 and j >= 6):
                if grid[i][j] != "#":
                    return False
            # 左上及び右下の3x3領域に隣接する14マスはすべて白（.）である。
            elif (i < 3 and j == 3) or (i == 0 and 0 <= j <= 3) or (i == 5 and 5 <= j <= 8) or (5 < i < 9 and j == 5):
                if grid[i][j] != ".":
                    return False
    return True

def solve():
    N, M = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    ans = []

    for i in range(N - 8):
        for j in range(M - 8):
            grid = [row[j:j+9] for row in S[i:i+9]]
            if is_tak_code(grid):
                ans.append((i+1, j+1))

    for pos in ans:
        print(*pos)

solve()




