# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st=[]
        n=0
        curr=root
        while st or curr:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            n+=1
            if n==k:
                return curr.val
            curr=curr.right