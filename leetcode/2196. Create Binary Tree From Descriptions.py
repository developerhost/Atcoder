# Definition for a binary tree node.
# descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

"""
setdefault() メソッドは、辞書（dictionary）オブジェクトにキーが存在しない場合に、指定したデフォルト値を設定し、その値を返すメソッドです。

setdefault() メソッドの構文は以下の通りです：

dict.setdefault(key, default_value)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val_to_node, kids = {}, set()  # 値とノードの対応関係と子ノードのセットを初期化

        for parent, kid, left in descriptions: # 親ノード、子ノード、左右の情報を取得
            kids.add(kid)  # 子ノードをセットに追加

            parent_node = val_to_node.setdefault(parent, TreeNode(parent))  # 親ノードが存在しない場合は新しいノードを作成し、辞書に追加
            kid_node = val_to_node.setdefault(kid, TreeNode(kid))  # 子ノードが存在しない場合は新しいノードを作成し、辞書に追加

            if left == 1:
                parent_node.left = kid_node  # 左の子ノードとして設定
            else:
                parent_node.right = kid_node  # 右の子ノードとして設定

        return val_to_node[(val_to_node.keys() - kids).pop()]  # 根ノードを返す
