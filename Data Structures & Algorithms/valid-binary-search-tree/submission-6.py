# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        queue=deque([(root,float("-inf"),float("inf"))])

        while queue:
            cur,left,right=queue.popleft()

            if not (left<cur.val<right):
                return False
            if cur.left:
                queue.append([cur.left,left,cur.val])
            if cur.right:
                queue.append([cur.right,cur.val,right])
        return True

        