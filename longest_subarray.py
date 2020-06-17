from typing import List

def longestSubarray(nums: List[int], limit: int) -> int:
    longest_subar = 1
    if len(nums) == 0 or limit < 0:
        return 0
    
    diffs = []
    def check_diffs(num: int) -> int:
        for i in range(len(diffs)):
            if abs(diffs[i]-num) > limit:
                return i
        return -1
        
    for i in range(len(nums)):
        idx = check_diffs(nums[i])
        if idx >= 0:
            longest_subar = max(longest_subar, len(diffs))
            diffs = diffs[(idx+1):]
        diffs.append(nums[i])
        
    return longest_subar

longestSubarray([10,1,2,4,7,2], 5)