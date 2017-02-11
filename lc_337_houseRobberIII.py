from lc_util import *

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_(root):
            if root == None:
                return (0, 0)
            leftVal = rob_(root.left)
            rightVal = rob_(root.right)
            valWithNode = root.val + leftVal[1] + rightVal[1]
            valWithOutNode = leftVal[0] + rightVal[0]
            return (max(valWithOutNode, valWithNode), valWithOutNode)

        maxVal = rob_(root)
        return max(maxVal[0], maxVal[1])


null = 'null'
rep = [5,4,7,3,null,2,null,-1,null,9]
binTree = BinaryTreeGenerator.generateBinaryTree(BinaryTreeGenerator, rep)
print(Solution.rob(Solution, binTree))