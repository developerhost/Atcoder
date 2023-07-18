from typing import List

def main():
    n, t, m = map(int, input().split())
    bad = [[False]*n for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        bad[a][b] = True
        bad[b][a] = True

    ans = 0
    team = []

    def f(i):
        nonlocal ans, team
        if i == n:
            if len(team) == t:
                ans += 1
            return

        for j in range(len(team)):
            ok = True
            for p in team[j]:
                if bad[i][p]:
                    ok = False
            if not ok:
                continue
            team[j].append(i)
            f(i+1)
            team[j].pop()

        team.append([i])
        f(i+1)
        team.pop()

    f(0)

    print(ans)

if __name__ == '__main__':
    main()
