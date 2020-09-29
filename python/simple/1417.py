"""
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。
请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。
请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。

示例 1：
输入：s = "a0b1c2"
输出："0a1b2c"
解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。

示例 2：
输入：s = "leetcode"
输出：""
解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。

示例 3：
输入：s = "1229857369"
输出：""
解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。

示例 4：
输入：s = "covid2019"
输出："c2o0v1i9d"

示例 5：
输入：s = "ab123"
输出："1a2b3"

提示：
1 <= s.length <= 500
s 仅由小写英文字母和/或数字组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reformat-the-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reformat(self, s: str) -> str:
        chars, digits = [ch for ch in s if ch.isalpha()], [ch for ch in s if ch.isdigit()]
        len_char, len_digit = len(chars), len(digits)
        if abs(len_char - len_digit) > 1:
            return ''
        if len_char > len_digit:
            return ''.join((chars[i] + str(digits[i])) for i in range(len_digit)) + chars[len_char - 1]
        elif len_char == len_digit:
            return ''.join((str(digits[i]) + chars[i]) for i in range(len_char))
        else:
            return ''.join((str(digits[i]) + chars[i]) for i in range(len_char)) + digits[len_digit - 1]


if __name__ == '__main__':
    print(Solution().reformat("covid2019"))
