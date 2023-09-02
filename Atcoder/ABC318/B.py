def main():
    # グリッドの初期化
    grid = [[0 for _ in range(100)] for _ in range(100)]
    
    N = int(input())

    for _ in range(N):
        A, B, C, D = map(int, input().split())
        
        # シートによって覆われているセルをマークする
        for x in range(A, B):
            for y in range(C, D):
                grid[x][y] = 1

    # マークされたセルの数をカウントする
    ans = sum(row.count(1) for row in grid)

    print(ans)

if __name__ == '__main__':
    main()
