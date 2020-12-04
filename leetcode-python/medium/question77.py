"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入:n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def find_combine(nums: List[int], start_num: int):
            if len(nums) == k:
                result.append(nums)
                return
            for i in range(start_num, n + 1):
                find_combine(nums + [i], i + 1)

        result = []
        find_combine([], 1)
        return result

    def combinev2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    assert [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]] == Solution().combine(4, 2)
    assert [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]] == Solution().combinev2(4, 2)
