import io
import sys

_INPUT = """\
4
1 5 4
7 8
6
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    N = int(input())
    D = [[0] * N for _ in range(N)]
    for i in range(N-1):
        row = list(map(int, input().split()))
        for j in range(i+1, N):
            D[i][j] = D[j][i] = row[j - i - 1]

    answer = 0
    # (1<<N)は2^Nと同じ意味で、可能な状態の数を示している
    for state in range(1<<N):
        total = 0
        for i in range(N):
            for j in range(i+1, N):
                # i番目とj番目の頂点が両方選択されているかどうか
                if (state & (1<<i)) and (state & (1<<j)):
                    total += D[i][j]
        answer = max(answer, total)
        print(state, total)

    print(answer)

if __name__ == "__main__":
    main()
