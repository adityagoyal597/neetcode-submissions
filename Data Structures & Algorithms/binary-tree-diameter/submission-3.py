# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0


        def dfs(curr):
            if not curr:
                return 0

            left=dfs(curr.left)
            right=dfs(curr.right)

            # res keeps track of the max diameter found
            self.res=max(self.res,left+right)
            
            return 1+max(left,right) # returns the height to the parent
        
        dfs(root)

        return self.res
            