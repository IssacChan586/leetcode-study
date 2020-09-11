"""
找出所有相加之和为n 的k个数的组合。组合中只允许含有 1 -9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

import validator


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(cur_nums=[], leaving=n, cur_idx=1):
            len_cur = len(cur_nums)
            if len_cur == k:
                if leaving == 0:
                    result.append(cur_nums)
                return
            for i in range(cur_idx, 10):
                if (leaving - i < 0) or (10 - i < k - len_cur) or (leaving > leaving_sum[10 - k + len_cur]):
                    # condition1: leaving比i小，后续任意数字加上都会超
                    # condition2: 剩余数字全选上，总数量仍然达不到预期数量n;
                    # condition3: 剩余数字总和 > sum(i,9),即 全部加上也达不到leaving
                    break
                backtracking(cur_nums + [i], leaving - i, i + 1)

        leaving_sum = [0, 45, 44, 42, 39, 35, 30, 24, 17, 9]
        result = []
        backtracking()
        return result


if __name__ == '__main__':
    validator.validate_without_order(Solution().combinationSum3(3, 7), [[1, 2, 4]])
    validator.validate_without_order(Solution().combinationSum3(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
    validator.validate_without_order(Solution().combinationSum3(3, 100), [])
    validator.validate_without_order(Solution().combinationSum3(9, 46), [])
    validator.validate_without_order(Solution().combinationSum3(2, 6), [[1, 5], [2, 4]])
