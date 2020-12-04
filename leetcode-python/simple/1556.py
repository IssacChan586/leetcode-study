"""
给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。

示例 1：
输入：n = 987
输出："987"

示例 2：
输入：n = 1234
输出："1.234"

示例 3：
输入：n = 123456789
输出："123.456.789"

示例 4：
输入：n = 0
输出："0"

提示：
0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/thousand-separator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        new_s, count = [], 0
        while n > 0:
            new_s.insert(0, str(n % 10))
            n //= 10
            count += 1
            if count % 3 == 0:
                new_s.insert(0, '.')
        if new_s[0] == '.':
            del new_s[0]
        return ''.join(new_s)


if __name__ == '__main__':
    assert Solution().thousandSeparator(123456789) == "123.456.789"
    assert Solution().thousandSeparator(0) == "0"
