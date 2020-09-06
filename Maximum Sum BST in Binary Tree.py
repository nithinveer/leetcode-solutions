# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max = 0

    def dfs(self, node):
        print(node.val, self.max, node)
        if node.left is None and node.right is None:
            self.max = max(self.max, node.val)
            return True, node.val
        elif node.left is not None and node.right is not None:
            # print(node.val, self.max)
            leftB, leftVal = self.dfs(node.left)
            rightB, rightVal = self.dfs(node.right)
            # print(node.val, rightVal, leftVal)
            if node.left.val < node.val < node.right.val and leftB and rightB:
                self.max = max(self.max, node.val + rightVal + leftVal)
                return True, node.val + rightVal + leftVal
            else:
                if node.left.val < node.val and leftB:
                    self.max = max(self.max, leftVal)
                    return False, leftVal
                if node.right.val > node.val and rightB:
                    self.max = max(self.max, rightVal)
                    return False, rightVal
        elif node.left is None:
            rightB, rightVal = self.dfs(node.right)
            if node.right.val > node.val and rightB:
                self.max = max(self.max, rightVal + node.val)
                return False, rightVal + node.val
        else:
            leftB, leftVal = self.dfs(node.left)
            if node.left.val < node.val and leftB:
                self.max = max(self.max, leftVal + node.val)
                return False, leftVal + node.val

    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.max
