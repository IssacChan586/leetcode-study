"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
返回可以通过分割得到的平衡字符串的最大数量。

示例 1：
输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。

示例 2：
输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。

示例 3：
输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".

提示：
1 <= s.length <= 1000
s[i] = 'L' 或 'R'
分割得到的每个字符串都必须是平衡字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_r, count = {'L': 0, 'R': 0}, 0
        for ch in s:
            l_r[ch] += 1
            if l_r['L'] == l_r['R']:
                count, l_r = count + 1, {'L': 0, 'R': 0}
        return count


if __name__ == '__main__':
    assert Solution().balancedStringSplit("RLRRLLRLRL") == 4
    assert Solution().balancedStringSplit("RLLLLRRRLR") == 3
    assert Solution().balancedStringSplit("LLLLRRRR") == 1
