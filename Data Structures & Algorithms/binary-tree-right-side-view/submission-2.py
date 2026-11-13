from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        def levelOrder(node):
            while queue:
                len_level = len(queue)
                level = []
                
                for _ in range(len_level):

                    popped = queue.popleft()
                    level.append(popped.val)
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
                    
                ans.append(level[-1])
        levelOrder(root)
        return ans
