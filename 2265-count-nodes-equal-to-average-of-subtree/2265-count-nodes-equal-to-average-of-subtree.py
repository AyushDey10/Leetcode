# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]

        def dfs(node):
            if node is None:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total = left_sum + right_sum + node.val
            count = left_count + right_count + 1

            if total // count == node.val:
                ans[0] += 1

            return total, count

        dfs(root)
        return ans[0]