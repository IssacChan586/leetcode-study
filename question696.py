"""
给定一个字符串  s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。

示例 1 :
输入: "00 11 00 11"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
请注意，一些重复出现的子串要计算它们出现的次数。
另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。

注意：
s.length  在1到50,000之间。
s 只包含“0”或“1”字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        """
        按照连续0,连续1分割出不同的段落,连续段落中取min累加
        如 00111 -> [2,3] -> 01 0011 = 2
        """
        count_list = []
        # 末尾补1位不同字符方便统计
        s = s + '#'
        cur_count, last_count, total_count = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_count = cur_count + 1
            else:
                total_count = total_count + min(last_count, cur_count)
                last_count = cur_count
                cur_count = 1
        return total_count


if __name__ == '__main__':
    assert 6 == Solution().countBinarySubstrings("00110011")
    assert 4 == Solution().countBinarySubstrings("10101")
