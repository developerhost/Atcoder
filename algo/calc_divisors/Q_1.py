# print("Hello World!")
def divirse(N):
    res = []
    for i in range(1, N+1):
        if i * i > N:
            break
        if N % i != 0:
            continue # 処理をスキップする
        res.append(i)

        if N // i != i:
            res.append(N // i)
    # print(res)
    print(len(res))



divirse(56)
