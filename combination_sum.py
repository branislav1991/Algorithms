from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    def recur(i, target, solution):
        if target < 0:
            return []
        if i >= len(candidates):
            return []
        if candidates[i] == target:
            first = [sorted(solution + [candidates[i]])]
            second = [sorted(s) for s in recur(i+1, target, solution)]
            first.extend(x for x in second if x not in first)
            return first
        elif candidates[i] > target:
            return recur(i+1, target, solution)
        else:
            first = [sorted(s) for s in recur(i+1, target, solution)]
            second = [sorted(s) for s in recur(i+1, target-candidates[i], solution + [candidates[i]])]
            first.extend(x for x in second if x not in first)
            return first
        
    sol = recur(0, target, [])
    return sol

print(combinationSum2([10,1,2,7,6,1,5], 8))