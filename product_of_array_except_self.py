from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = []
        start = 1
        for i in range(len(nums)):
            start = start * nums[i]
            new.append(start//nums[i])
        return new


sol = Solution()
print(sol.productExceptSelf(nums=[1,2,3]))