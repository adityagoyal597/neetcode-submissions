# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # reach a null poition , nothing to be deleted , key doesn't exist
            return root

        # searching the key
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        
        # key found 
        else:
            if not root.left: #0/1 children
                return root.right
            elif not root.right:#0/1 children
                return root.left
            
            # else the node to be deleted has two children 
            curr=root.right #2 children , replacing rootnode with min value from the right subtree
            
            while curr and curr.left:
                curr=curr.left
            
            root.val=curr.val
            root.right=self.deleteNode(root.right,curr.val)
        
        return root
            