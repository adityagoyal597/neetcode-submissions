class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path=[]
        def Path(root,path):
            if not root: # base case: null node
                return False
            path.append(root.val)
            if not root.left and not root.right: # leaf node
                res = (targetSum==sum(path))
                if not res: 
                    path.pop()
                return res # return true if targrtsum==sum of the path
            if Path(root.left,path):
                return True
            if Path(root.right,path):
                return True
            path.pop()
            return False
        return Path(root,path)