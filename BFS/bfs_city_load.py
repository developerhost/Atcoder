'''
問題
N個の街とN-1本の道路からなる街があります。i番目の道路は街Aiと街Biを双方向に結んでいます。
また、どの2つの街の間も、いくつかの道路を通って移動可能な経路が存在します。
道路はすべて同じ長さです。

Q個のクエリが与えられるので、各クエリについて以下の値を求めてください。

現在高橋くんは街ciに、青木くんは街diにいます。
二人が同時に街を出発し、同じタイミングで同じ速さで街を移動するとき、
二人が街で出会うか道路上で出会うかを判定してください。
'''

# input
N = 4
Q = 1

li = [[1, 2], [2, 3], [2, 4]]

# ノードの隣接リストを作成する
graph = [[] for _ in range(N)]
for i in li:
    print(i)
    graph[i[0]-1].append(i[1]-1)
    graph[i[1]-1].append(i[0]-1)

# どことどこがつながっているかを表示する
print(graph)

from collections import deque
d = deque([0]) # キューを作成する
distance = [-1] * N # 訪問済みのノードには訪問しないようにする -1は未訪問
distance[0] = 0

# 訪問済みのノードを管理する
# 初期値は0, 0のノードから伸びている道路の先を訪問リストであるdequeに追加する
while d:
    x = d.popleft() # キューから先頭の要素を取り出す
    for i in graph[x]:
        print(i)
        if distance[i] == -1: # 未訪問の場合
            distance[i] = distance[x] + 1 # 訪問済みにして、距離を入れる
            d.append(i) # 訪問済みのノードをキューに追加する
print(distance, d)

for i in range(Q): # クエリの数だけ繰り返す
    c = 2 # 高橋くんのいる街
    d = 4 # 青木くんのいる街
    if (distance[c-1] + distance[d-1]) % 2 == 0: # 距離の偶奇で判定する
        print('Town') # 偶数の場合は街
    else:
        print('Road') # 奇数の場合は道路