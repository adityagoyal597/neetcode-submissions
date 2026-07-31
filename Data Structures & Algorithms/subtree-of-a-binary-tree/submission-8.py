# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helpper Function
        def sameTree(root,subRoot):

            # both null 
            if not root and not subRoot:
                return True

            # both non null and all values same
            if root and subRoot and root.val==subRoot.val:
                return(sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right))
            
            # else-> one is non null and other is null
            return False # can't be same

        
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False

        # both are non null

        if sameTree(root,subRoot):
            return True

        return(self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))



        