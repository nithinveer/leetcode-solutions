# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        que = []
        que.append(root)
        
        while len(que) >0:
            tmp_q = []
            sum = 0
            for each_ in que:
                sum += each_.val
                if each_.left is not None :
                    tmp_q.append(each_.left)
                if each_.right is not None :
                    tmp_q.append(each_.right)
            
            que = tmp_q
        
        return sum
                
            