# 移动零到数组右端
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i] # 交换
                i0 += 1
                
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    
    sol = Solution()
    sol.moveZeroes(nums)
    
    print(' '.join(map(str, nums)))