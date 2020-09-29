"""
给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。
「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。

示例 1：
输入：s = "011101"
输出：5
解释：
将字符串 s 划分为两个非空子字符串的可行方案有：
左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5
左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4
左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3
左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2
左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3

示例 2：
输入：s = "00111"
输出：5
解释：当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5

示例 3：
输入：s = "1111"
输出：3
 
提示：
2 <= s.length <= 500
字符串 s 仅由字符 '0' 和 '1' 组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxScore(self, s: str) -> int:
        import collections
        count, max_score = collections.Counter(s), 0
        last_left_score, last_right_score = 0, count['1']
        for i in range(0, len(s) - 1):
            if s[i] == '0':
                last_left_score += 1
            else:
                last_right_score -= 1
            max_score = max(max_score, last_left_score + last_right_score)
        return max_score


if __name__ == '__main__':
    assert Solution().maxScore("011101") == 5
    assert Solution().maxScore("00111") == 5
    assert Solution().maxScore("1111") == 3
