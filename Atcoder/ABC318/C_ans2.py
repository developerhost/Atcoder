N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True) 
cost = 0
for i in range(0, N, D):
    group_sum = sum(F[i:min(i + D, N)])
    cost += min(P, group_sum)

print(cost)