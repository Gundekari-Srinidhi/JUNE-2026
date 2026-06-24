# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node)
            preorder(node.left)
            preorder(node.right)
            return res

        val = preorder(root)
        ans = []
        for i in range(len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]        
        