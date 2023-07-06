"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""

このコードは、与えられた木の最大の深さを求めるための解決策です。
maxDepthメソッドは、与えられたルートノードから始まる木の最大深さを計算します。
与えられたノードが存在しない場合、つまりルートがNoneの場合、深さは0です。

キューを使用して、幅優先探索（BFS）を実装しています。
キューには、現在のノードとその深さがタプルとして格納されます。
最初にルートノードと深さ1をキューに追加し、ループを開始します。
キューが空になるまで、以下の処理を繰り返します：

キューの先頭からノードとその深さを取得します。
現在の深さを最大の深さとして更新します。
現在のノードに子ノードがある場合、それぞれの子ノードと現在の深さ+1をキューに追加します。
最終的に、最大の深さが返されます。
"""

from collections import deque

from yaml import Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        nodes = deque()  # ノードを格納するキューを作成します
        nodes.append((root, 1))  # ルートノードとその深さ（1）をキューに追加します
        maxx = 0  # 最大の深さを保持する変数を初期化します

        while nodes:  # キューが空でない限り繰り返します
            current, val = nodes.popleft()  # キューの先頭からノードとその深さを取得します
            maxx = val  # 現在の深さを最大の深さとして更新します
            if current.children:  # 子ノードがある場合は処理を行います
                for child in current.children:  # 子ノードを順番に処理します
                    nodes.append((child, val+1))  # 子ノードと現在の深さ+1をキューに追加します
        return maxx  # 最大の深さを返します
