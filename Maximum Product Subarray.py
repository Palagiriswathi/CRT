class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        l=1
        r=1
        maxi = float('-inf')
        for i in range(n):
            l *= nums[i]
            r  *=nums[n - i - 1]
            maxi = max(maxi, l, r)
            if l == 0:
                l = 1
            if r == 0:
                r = 1
        return maxi            
