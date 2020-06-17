from typing import List

def search(nums: List[int], target: int) -> int:
    def quicksearch(i, j):
        if j <= i:
            return False
        
        pivot = nums[(j+i)//2]
        if target == pivot:
            return True
        else:
            return quicksearch(i, (j+1)//2) or quicksearch((j+i)//2+1, j)
        
    return quicksearch(0, len(nums))

print(search([2,5,6,0,0,1,2], 3))