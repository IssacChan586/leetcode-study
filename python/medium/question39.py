"""
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的数字可以无限制重复被选取。

说明：
所有数字（包括target）都是正整数。
解集不能包含重复的组合。

示例1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
]

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(cur_nums=[], leaving_target=target, cur_idx=0):
            if cur_idx == len(candidates):
                return
            if leaving_target == 0:
                result.append(cur_nums)
                return
            backtracking(cur_nums, leaving_target, cur_idx + 1)
            if leaving_target - candidates[cur_idx] >= 0:
                backtracking(cur_nums + [candidates[cur_idx]], leaving_target - candidates[cur_idx], cur_idx)

        result = []
        backtracking()
        return result

    def combinationSumV2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(cur_nums=[], cur_sum=0, start_index=0):
            if len(cur_nums) > 30 or cur_sum > target:
                return
            if cur_sum == target:
                result.append(cur_nums)
                return
            for i in range(start_index, len(candidates)):
                backtracking(cur_nums + [candidates[i]], cur_sum + candidates[i], i)

        result = []
        backtracking()
        return result


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
    print(Solution().combinationSum([3, 12, 9, 11, 6, 7, 8, 5, 4], 15))
