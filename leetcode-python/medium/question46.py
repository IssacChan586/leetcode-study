"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

import validator


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(leaving_nums: List[int], cur_nums=list()):
            if len(leaving_nums) == 0:
                result.append(cur_nums[:])
                return
            for num in leaving_nums:
                cur_nums.append(num)
                ori_index = leaving_nums.index(num)
                leaving_nums.remove(num)
                backtracking(leaving_nums, cur_nums)
                leaving_nums.insert(ori_index, num)
                cur_nums.remove(num)

        result = []
        backtracking(nums)
        return result


if __name__ == '__main__':
    validator.validate_without_order(Solution().permute([1, 2, 3]),
                                     [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
