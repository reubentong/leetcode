from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]

sol = Solution()
print(sol.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3))