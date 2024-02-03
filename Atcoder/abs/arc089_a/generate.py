#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    t = [None for _ in range(N)]
    x = [None for _ in range(N)]
    y = [None for _ in range(N)]
    for i in range(N):
        t[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        x[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        y[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N)
    for i in range(N):
        print(t[i], x[i], y[i])

if __name__ == "__main__":
    main()
