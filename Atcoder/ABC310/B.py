# Wrong Answer
N, M = map(int, input().split())
items = []
for _ in range(N):
    data = list(map(int, input().split()))
    price = data[0]
    features = 0
    for f in data[2:]:
        features |= 1 << (f - 1)
    items.append((price, features))

answer = "No"
for i in range(N):
    for j in range(N):
        if i != j:
            if items[i][0] >= items[j][0] and (items[i][1] & items[j][1]) == items[j][1]:
                if items[i][0] > items[j][0] or items[i][1] != items[j][1]:
                    answer = "Yes"
                    break
    if answer == "Yes":
        break

print(answer)


# another
N, M = map(int, input().split())
items = []
for _ in range(N):
    item = list(map(int, input().split()))
    items.append((item[0], set(item[2:])))

for i in range(N):
    for j in range(i+1, N):
        if (items[i][0] >= items[j][0] and items[j][1].issubset(items[i][1]) and (items[i][0] > items[j][0] or not items[i][1].issubset(items[j][1]))) or (items[i][0] <= items[j][0] and items[i][1].issubset(items[j][1]) and (items[i][0] < items[j][0] or not items[j][1].issubset(items[i][1]))):
            print('Yes')
            exit(0)
print('No')

