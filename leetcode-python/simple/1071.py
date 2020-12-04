"""
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

示例 2：
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"

示例 3：
输入：str1 = "LEET", str2 = "CODE"
输出：""

提示：
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ''

    def gcdOfStringsV2(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                if str1[0:i] * (len(str1) // i) == str1 and str1[0:i] * (len(str2) // i) == str2:
                    return str1[0:i]
        return ''


if __name__ == '__main__':
    assert Solution().gcdOfStrings(str1="ABCABC", str2="ABC") == "ABC"
    assert Solution().gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
    assert Solution().gcdOfStrings(str1="LEET", str2="CODE") == ""
    assert Solution().gcdOfStrings(str1="LEET", str2="LEET") == "LEET"
    assert Solution().gcdOfStrings(str1="LEET", str2="LEETLEET") == "LEET"
    assert Solution().gcdOfStrings(str1="ABAABAABA", str2="ABAABA") == "ABA"
