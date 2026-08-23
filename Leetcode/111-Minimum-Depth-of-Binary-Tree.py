# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepthSoFar = 0
        stack = [(root, 0)]
        while (len(stack)):
            nodeToExplore = stack.pop()
            node = nodeToExplore[0]
            currentDepth = nodeToExplore[1]

            if (not node):
                continue

            currentDepth += 1
            if (not node.right and not node.left):
                minDepthSoFar = currentDepth if currentDepth < minDepthSoFar or minDepthSoFar == 0 else minDepthSoFar
            else:
                stack.append((node.right, currentDepth))
                stack.append((node.left, currentDepth))
        return minDepthSoFar

