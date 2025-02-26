from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        planted = 0

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                planted += 1
                if planted >= n:
                    return True

        return planted >= n

sol = Solution()
print(sol.canPlaceFlowers([0,0,1,0], 2))