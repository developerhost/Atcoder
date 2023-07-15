# correct answer
import io
import sys

_INPUT = """\
4 4
3 1 1
3 1 2
3 1 2
4 2 2 3
"""
sys.stdin = io.StringIO(_INPUT)

def solve(N, M, items):
    for i in range(N):
        for j in range(N):
            if i != j:
                Pi, Ci, Fi = items[i]
                Pj, Cj, Fj = items[j]
                # Price and feature set are identical
                if Pi == Pj and Fi == Fj:
                    continue
                # Pi >= Pj and all features of j-th item are included in i-th item
                if Pi >= Pj and all(f in Fj for f in Fi):
                    print(i, j)
                    print(Pi, Pj)
                    print(Fi, Fj)
                    if Pi > Pj or any(f not in Fi for f in Fj):
                        print(i, j)
                        return "Yes"
    return "No"

def main():
    N, M = map(int, input().split())
    items = []
    for _ in range(N):
        item = list(map(int, input().split()))
        P, C, F = item[0], item[1], item[2:]
        items.append((P, C, set(F)))  # store features as a set for easier comparison
    print(solve(N, M, items))

if __name__ == "__main__":
    main()
