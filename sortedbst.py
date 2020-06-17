from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if not nums:
        return None
    
    def make_tree(i, j):
        if j <= i:
            return None
        
        val = nums[(j+i)//2]
        left = make_tree(i, (i+j)//2)
        right = make_tree((i+j)//2+1, j)
        return TreeNode(val, left, right)
    
    return make_tree(0, len(nums))

sortedArrayToBST([-10,-3,0,5,9])