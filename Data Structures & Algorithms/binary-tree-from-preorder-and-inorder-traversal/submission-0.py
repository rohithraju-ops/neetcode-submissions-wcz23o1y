# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}
        for i, val in enumerate(inorder):
            indexMap[val] = i
        
        self.p = 0
        
        def build(left, right):
            
            if left > right:
                return None
                
            root = TreeNode(preorder[self.p])
            self.p += 1
            
            i = indexMap[root.val]
            root.left = build(left, i - 1)
            root.right = build(i + 1, right)
            return root 
            
        return build(0, len(inorder) - 1 )
        