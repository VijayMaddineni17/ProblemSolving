class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

import unittest
from collections import deque,defaultdict
class binaryTreeVerticalOrdering:
    
    def __init__(self, root:TreeNode):
        self.root=root
    
    def printVerticalColumns(self):
        q=deque()
        dic=defaultdict(list)
        q.append((self.root,0))
        res=[]
        while q:
            
            node,level=q.popleft()
            dic[level].append(node.value)
            
            if node.left:
                # dic[level-1].append(node.left.value)
                q.append((node.left,level-1))
            if node.right:
                # dic[level+1].append(node.right.value)
                q.append((node.right,level+1))
            
    
        for key in sorted(dic.keys()):
            for v in dic[key]:
                res.append(v)
        print(dic)
        return res

class TestBinaryTreeVerticalOrdering(unittest.TestCase):
    
    def test_example_case(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        tree = binaryTreeVerticalOrdering(root)
        expected_output = [
            4,        # First column
            2,        # Second column
            1, 5, 6,  # Third column
            3,        # Fourth column
            7         # Fifth column
        ]
        self.assertEqual(tree.printVerticalColumns(), expected_output)

if __name__=='__main__':
    unittest.main()
                
            
            
        
        
        