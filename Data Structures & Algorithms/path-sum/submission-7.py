class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path=[]
        def Path(root,path):
            if not root:
                return False
            path.append(root.val)
            if not root.left and not root.right:
                res = (targetSum==sum(path))
                if not res: path.pop()
                return res
            if Path(root.left,path):
                return True
            if Path(root.right,path):
                return True
            path.pop()
            return False
        return Path(root,path)