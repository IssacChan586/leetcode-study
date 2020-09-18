"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(cur_nums: List[int], used: List[bool]) -> None:
            if len(cur_nums) == len(nums):
                ans.append(cur_nums)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    backtracking(cur_nums + [nums[i]], used)
                    used[i] = False

        nums.sort()
        ans = []
        backtracking([], [False for _ in range(len(nums))])
        return ans

    def permuteUniqueV2(self, nums: List[int]) -> List[List[int]]:
        def backtracking(cur_nums: List[int], leaving_nums: List[int]):
            if len(leaving_nums) == 0:
                if cur_nums not in ans:
                    ans.append(cur_nums)
                return
            for i in range(len(leaving_nums)):
                origin_num = leaving_nums[i]
                del leaving_nums[i]
                backtracking(cur_nums + [origin_num], leaving_nums)
                leaving_nums.insert(i, origin_num)

        ans = list()
        backtracking([], nums)
        return ans


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
