"""
给定一组不含重复元素的整数数组nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from python import validator


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def search(cur_nums: List[int], start_index: int, total_count: int):
            if len(cur_nums) == total_count:
                result.append(cur_nums[:])
                return
            for i in range(start_index, len(nums)):
                cur_nums.append(nums[i])
                search(cur_nums, i + 1, total_count)
                cur_nums.remove(nums[i])

        result = []
        for n in range(len(nums) + 1):
            search([], 0, n)
        return result


if __name__ == '__main__':
    validator.validate_without_order(Solution().subsets([1, 2, 3]),
                                     [[1], [3], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []])
