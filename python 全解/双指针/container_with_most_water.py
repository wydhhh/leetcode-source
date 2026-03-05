# 盛水最多的容器
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1 #左边短，动左端
            else:
                res = max(res, height[j] * (j - i))
                j -= 1 #右边短，动右端
        return res
    
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    
    sol = Solution()
    ans = sol.maxArea(nums)
    
    print(ans)