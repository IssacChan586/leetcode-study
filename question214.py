"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例1:
输入: "aacecaaa"
输出: "aaacecaaa"

示例 2:
输入: "abcd"
输出: "dcbabcd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        for fill_len in range(len(s)):
            s_new = ""
            for i in range(fill_len):
                s_new = s_new + s[len(s) - i - 1]
            s_new = s_new + s
            if len(s_new) % 2 == 0:
                # 新字符串为双中心, 如 8 选 3,4
                left, right = len(s_new) // 2 - 1, len(s_new) // 2
            else:
                # 新字符串为单中心, 如 9 选 3,5
                left, right = len(s_new) // 2 - 1, len(s_new) // 2 + 1
            while left >= 0 and right < len(s_new) and s_new[left] == s_new[right]:
                left = left - 1
                right = right + 1
            if right == len(s_new):
                return s_new


if __name__ == '__main__':
    assert "" == Solution().shortestPalindrome("")
    assert "a" == Solution().shortestPalindrome("a")
    assert "bab" == Solution().shortestPalindrome("ab")
    assert "aaacecaaa" == Solution().shortestPalindrome("aacecaaa")
    assert "dcbabcd" == Solution().shortestPalindrome("abcd")
