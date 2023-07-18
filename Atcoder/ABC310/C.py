# AC
N = int(input())
balls = set()

for _ in range(N):
    S = input().strip() # strip() で文字列の前後の空白を削除
    # Sを逆順にした文字列（S[::-1]）
    if S not in balls and S[::-1] not in balls:
        balls.add(S)

print(len(balls))
