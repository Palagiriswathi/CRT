class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = []

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            result.append(product)

        return result


nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))