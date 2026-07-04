from typing import List  # Needed for type annotations

class Solution:
    def generate(self, ind, curr_subset, ans, candidates, target):
        if target == 0: 
            ans.append(curr_subset.copy())
            return
        if target < 0:
            return
        if ind == len(candidates):
            return
        
        # Include current candidate
        curr_subset.append(candidates[ind])
        self.generate(ind, curr_subset, ans, candidates, target - candidates[ind])
        
        # Backtrack and try next candidate
        curr_subset.pop()
        self.generate(ind + 1, curr_subset, ans, candidates, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ind = 0  
        curr_subset = []
        ans = []
        self.generate(ind, curr_subset, ans, candidates, target)
        return ans
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))  # Output: [[2, 2, 3], [7]]
    