
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printTree(self):
        print(self.val, end='')
        print('(', end='')
        if self.left == None:
            print('null', end='')
        else:
            self.left.printTree()
        print(',', end='')
        if self.right == None:
            print('null', end='')
        else:
            self.right.printTree()
        print(')', end='')

class BinaryTreeGenerator(object):
    def generateBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None
        root = TreeNode(nodes[0])
        if root == 'null':
            return None
        q = [root]
        ind = 1
        length = len(nodes)
        while ind < length:
            pNode = q.pop(0)
            if (ind < length and nodes[ind] != 'null'):
                left = TreeNode(nodes[ind])
                q.append(left)
            else:
                left = None
            if (ind + 1 < length  and nodes[ind + 1] != 'null'):
                right = TreeNode(nodes[ind + 1])
                q.append(right)
            else:
                right = None
            pNode.left = left
            pNode.right = right
            ind +=2
        return root

    def test(self):
        null = 'null'
        rep = [5,4,7,3,null,2,null,-1,null,9]
        binTree = self.generateBinaryTree(self, rep)
        binTree.printTree()


# BinaryTreeGenerator.test(BinaryTreeGenerator)