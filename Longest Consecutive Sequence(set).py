class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)

        for num in numset:
            if num - 1 not in numset:
                curr = num
                le = 1

                while curr + 1 in numset:
                    curr += 1
                    le += 1

                longest = max(longest, le)

        return longest