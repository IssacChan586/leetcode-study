"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字1和0。

示例1:
输入: a = "11", b = "1"
输出: "100"

示例2:
输入: a = "1010", b = "1011"
输出: "10101"

提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            return self.addBinary(b, a)
        # 保证 len(a) <= len(b)
        a, b, ans = a[::-1], b[::-1], [0 for _ in range(len(b) + 1)]
        for i in range(len(b)):
            ans[i] += (int(a[i]) + int(b[i])) if i < len(a) else int(b[i])
            if ans[i] > 1:
                ans[i + 1] += ans[i] // 2
                ans[i] = ans[i] % 2
        ans.reverse()
        if ans[0] == 0:
            del ans[0]
        return ''.join(str(c) for c in ans)


if __name__ == '__main__':
    assert Solution().addBinary("0", "0") == "0"
    assert Solution().addBinary("0", "1") == "1"
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary("1010", "1011") == "10101"
