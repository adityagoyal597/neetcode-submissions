# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def SameTree(root,subRoot):

            if not root and not subRoot:
                return True
            if root and subRoot and root.val==subRoot.val:
                return (SameTree(root.left,subRoot.left) and SameTree(root.right,subRoot.right))
            return False
        
        if not subRoot and root:
            return True
        
        if not root and subRoot:
            return False
        
        if SameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)