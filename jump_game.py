from typing import List

def jump(self, nums: List[int]) -> int:
    if len(nums) < 2: return 0
    
    tbl = {}
    tbl[0] = 0
    def min_steps(n):
        if n in tbl:
            return tbl[n]
        
        st = []
        for j in range(n-1, -1, -1):
            if nums[j] + j >= n:
                st.append(min_steps(j) + 1)
        return min(st)
    
    for i in range(1, len(nums)):
        tbl[i] = min_steps(i)
        
    return tbl[len(nums)-1]

jump([2,3,1,1,4])