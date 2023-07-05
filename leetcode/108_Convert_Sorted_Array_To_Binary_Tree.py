# Definition for a binary tree node.
from ast import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(nums, start, end):
            if start <= end:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = createTree(nums, start, mid-1)
                node.right = createTree(nums, mid+1, end)
                return node
        return createTree(nums, 0, len(nums) - 1)