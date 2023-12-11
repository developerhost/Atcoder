def is_prime(n):
  """nが素数かどうかを判定する関数"""
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True


def main():
  """素数を出力する関数"""
  n = int(input("n: "))
  for i in range(2, n + 1):
    if is_prime(i):
      print(i)


if __name__ == "__main__":
  main()