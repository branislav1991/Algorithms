class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val

    def __repr__(self):
        return str(self.val)

root = TreeNode(6)
l1 = TreeNode(5)
l11 = TreeNode(2)
l12 = TreeNode(5)
l2 = TreeNode(7)
l22 = TreeNode(8)
root.left = l1
root.right = l2
l1.parent = root
l2.parent = root
l1.left = l11
l1.right = l12
l2.right = l22
l11.parent = l1
l12.parent = l1
l22.parent = l2

s = []
def inorder_traversal(r: TreeNode):
    x = r
    while x is not None:
        s.append(x)
        x = x.left

    while len(s) > 0:
        x = s.pop()
        print(x)
        x = x.right
        while x is not None:
            s.append(x)
            x = x.left

inorder_traversal(root)