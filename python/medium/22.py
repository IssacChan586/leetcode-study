"""
数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(cur="", cur_left=0, cur_right=0):
            if cur_left == cur_right == n:
                result.append(cur)
                return
            for left in range(n - cur_left + 1):
                if left > 0:
                    backtracking(cur + "(", cur_left + 1, cur_right)
                for right in range(cur_left - cur_right - left + 1):
                    if right > 0:
                        backtracking(cur + ")", cur_left, cur_right + 1)

        result = []
        backtracking()
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
    # validator.validate_without_order(Solution().generateParenthesis(3),
    #                                  ["((()))", "(()())", "(())()", "()(())", "()()()"])
