"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from python import validator


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        非二分查找
        """
        left, right = -1, -1
        for idx, num in enumerate(nums):
            if num == target:
                if idx == 0:
                    left = 0
                elif nums[idx - 1] != target:
                    left = idx
                if idx == len(nums) - 1:
                    right = len(nums) - 1
                elif nums[idx + 1] != target:
                    right = idx
        return [left, right]


if __name__ == '__main__':
    validator.validate(Solution().searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
    validator.validate(Solution().searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
    validator.validate(Solution().searchRange([], 0), [-1, -1])
