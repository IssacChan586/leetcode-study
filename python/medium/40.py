"""
给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

示例1:
输入: candidates =[10,1,2,7,6,1,5], target =8,
所求解集为:
[[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]

示例2:
输入: candidates =[2,5,2,1,2], target =5,
所求解集为:
[[1,2,2], [5]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from python import validator


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(nums=[], leaving=target, cur_idx=0):
            if cur_idx > len(candidates):
                return
            if leaving == 0:
                if nums not in result:
                    result.append(nums)
                return
            for i in range(cur_idx, len(candidates)):
                if leaving < candidates[i]:
                    break

                if i > cur_idx and candidates[i] == candidates[i - 1]:
                    continue
                backtracking(nums + [candidates[i]], leaving - candidates[i], i + 1)

        result = list()
        candidates.sort()
        backtracking()
        return result


if __name__ == '__main__':
    validator.validate_without_order(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8),
                                     [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]])
    validator.validate_without_order(Solution().combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
    print(Solution().combinationSum2(
        [29, 19, 14, 33, 11, 5, 9, 23, 23, 33, 12, 9, 25, 25, 12, 21, 14, 11, 20, 30, 17, 19, 5, 6, 6, 5, 5, 11, 12, 25,
         31, 28, 31, 33, 27, 7, 33, 31, 17, 13, 21, 24, 17, 12, 6, 16, 20, 16, 22, 5], 28))
