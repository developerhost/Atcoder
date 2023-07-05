# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional


root = [1,2,3,4,5,6,7]
start = 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 		
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        print(graph)
        
        stack = [(root, None)]
        while stack: 
            n, p = stack.pop() # n = node, p = parent
            if p: 
                graph[p.val].append(n.val) # p.valは親の値。n.valは子の値, graphのkeyに親の値を入れて、valueに子の値を入れる
                graph[n.val].append(p.val) # graphのkeyに子の値を入れて、valueに親の値を入れる
            if n.left: stack.append((n.left, n)) # stackにはnodeとparentのタプルを入れる
            if n.right: stack.append((n.right, n))
        
        print(graph) # 現在のnodeから隣接しているnodeの辞書
        """
        defaultdict(<class 'list'>, 
        {
          1: [3, 5],
          3: [1, 6, 10],
          6: [3],
          10: [3],
          5: [1, 4],
          4: [5, 2, 9],
          2: [4],
          9: [4]
        }
        )
        """
        
        ans = -1
        seen = {start} # seenにはnodeの値を入れる
        queue = deque([start])
        while queue: # queueにはnodeの値を入れる
            for _ in range(len(queue)):  # queueの長さ分だけ繰り返す
                u = queue.popleft() # queueの先頭からnodeの値を取り出す
                for v in graph[u]:  # nodeの値に対応する隣接しているnodeの値を取り出す
                    if v not in seen:  # 隣接しているnodeの値がseenにない場合
                        seen.add(v) # seenに隣接しているnodeの値を追加する
                        queue.append(v) # queueに隣接しているnodeの値を追加する
            ans += 1
        return ans
  
Solution().amountOfTime(root, start)