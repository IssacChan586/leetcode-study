"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

    def isPalindromeV2(self, s: str) -> bool:
        def is_valid_char(ch: chr) -> bool:
            return 0 <= ord(ch) - ord('a') < 26 or 0 <= ord(ch) - ord('A') < 26 or 0 <= ord(ch) - ord('0') < 10

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not is_valid_char(s[left]):
                left += 1
            while left < right and not is_valid_char(s[right]):
                right -= 1
            # print('left: ', left, 'right: ', right, 's[left]:', s[left], 's[right]:', s[right])
            if 0 <= left < len(s) and 0 <= right < len(s) and s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")
    assert not Solution().isPalindrome("race a car")
    assert Solution().isPalindrome("race e car")
    assert Solution().isPalindrome("abcdcba")
    assert Solution().isPalindrome("abcddcba")
    assert Solution().isPalindrome("aaaa")
    assert Solution().isPalindrome("aaa")
    assert not Solution().isPalindrome("abaa")
    assert Solution().isPalindrome("")
    assert Solution().isPalindrome(".,")
    assert Solution().isPalindrome("\"Sue,\" Tom smiles, \"Selim smote us.\"")
