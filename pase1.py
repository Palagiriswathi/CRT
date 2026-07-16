class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        p = [0] * n
        s = [0] * n
        answer = [0] * n
        p[0] = nums[0]
        for i in range(1, n):
            p[i] = p[i-1] * nums[i]
        s[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            s[i] = s[i+1] * nums[i]
        answer[0] = s[1]
        answer[n-1] = p[n-2]
        for i in range(1, n-1):
            answer[i] = p[i-1] * s[i+1]
        return answer
nums = [1, 2, 3, 4]
obj = Solution() 
print(obj.productExceptSelf(nums))      
    