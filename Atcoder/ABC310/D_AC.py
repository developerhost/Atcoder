
n, t, m = map(int, input().split()) # n: 頂点の数, t: グループの数, m: 辺の数
ng = [[0] * n for _ in range(n)] # nxnの二次元リスト 頂点間の隣接行列 0: 隣接していない, 1: 隣接している
for _ in range(m):
  a, b = map(lambda x: int(x)-1, input().split()) # a, b: 頂点番号
  ng[a][b] = 1 # 隣接していることを記録
  ng[b][a] = 1 # 隣接していることを記録
ls = [[] for _ in range(t)] # t個のグループを作る グループごとに頂点番号を格納する
ans = 0

def dfs(i, l): # i: 頂点の番号, l: グループの番号
  global ans, n, t
  # print(ls, i, l)
  # print(i, l, t, n)
  if i == n: # 全ての頂点についてグループ分けが終わったら
    ans += len(ls[t-1]) > 0 # グループの数がtのものがあればansに1を足す
    return
  for j in range(l+1):
    flg = 0 # 隣接している頂点が既にグループに入っているかどうかを判定するフラグ
    for v in ls[j]:
      if ng[v][i]:
        flg = 1
        break
    if flg:
      continue
    ls[j].append(i)
    dfs(i+1, min(t-1, max(l, j+1)))
    ls[j].pop()

dfs(0, 0)
print(ans)