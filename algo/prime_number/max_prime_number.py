# N以下の最大の素数を求める

def max_prime_number(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n

N = 1000000007

# 判定
result = -1
# range(start, stop, step)
for i in range(N, 1, -1):
    if max_prime_number(i):
        result = i
        break
print(result)