# AC
N = int(input())
balls = set()

for _ in range(N):
    S = input().strip()
    if S not in balls and S[::-1] not in balls:
        balls.add(S)

print(len(balls))
