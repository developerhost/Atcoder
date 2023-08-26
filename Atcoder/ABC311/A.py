import io
import sys

_INPUT = """\
5
ACABB
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

# ABCが最初に現れる位置
abc = [0]*N
A = 0
B = 0
C = 0

for i in range(N):
    if S[i] == 'A':
        A = 1
    elif S[i] == 'B':
        B = 1
    else:
        C = 1
    
    if A == 1 and B == 1 and C == 1:
        print(i+1)
        break

# print(N, S)