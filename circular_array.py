from typing import List

def circularArrayLoop(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False
    
    for i in range(len(nums)):
        explored = [False for n in nums]
        explored[i] = True
        next_i = (i + nums[i]) % len(nums)
        positive = nums[i] > 0
        if next_i == i: # no cycle, because cyclelen == 1
            continue
            
        valid_cycle = True
        while not explored[next_i]:
            explored[next_i] = True
            if (nums[next_i] > 0) != positive: # no cycle
                valid_cycle = False
                break
            prev_i = next_i
            next_i = (next_i + nums[next_i]) % len(nums)
            if prev_i == next_i:
                valid_cycle = False
                break
                
        if valid_cycle:
            return True
        
    return False

print(circularArrayLoop([-1,-2,-3,-4,-5]))