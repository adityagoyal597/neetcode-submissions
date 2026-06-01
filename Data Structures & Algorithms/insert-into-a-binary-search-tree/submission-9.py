# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur=root

        while True:
            if val>cur.val:
                if not cur.right: #check till right node isn't null
                    cur.right=TreeNode(val)
                    return root
                else:
                    cur=cur.right

            else:
                if not cur.left:
                    cur.left=TreeNode(val)
                    return root
                else:
                    cur=cur.left