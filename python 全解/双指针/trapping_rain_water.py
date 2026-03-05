# 接雨水
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        sums = 0
        max_h = max(height)
        # 从第1层到最高层
        for h in range(1, max_h + 1):
            # 左：找到当前层左边第一个 >= 层高的位置
            while height[l] < h:
                l += 1
            # 右：找到当前层右边第一个 >= 层高的位置
            while height[r] < h:
                r -= 1
            sums += r - l + 1     # 总格子数增加当前高度的总格子数
        return sums - sum(height) # 总格子数 - 实心数 = 雨水数
    
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    
    sol = Solution()
    print(sol.trap(nums))