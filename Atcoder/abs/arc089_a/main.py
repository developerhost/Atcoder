#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(N: int, t: List[int], x: List[int], y: List[int]) -> str:
def solve(N, t, x, y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    t = [None for _ in range(N)]
    x = [None for _ in range(N)]
    y = [None for _ in range(N)]
    for i in range(N):
        t[i], x[i], y[i] = map(int, input().split())
    a = solve(N, t, x, y)
    print(a)

if __name__ == '__main__':
    main()
