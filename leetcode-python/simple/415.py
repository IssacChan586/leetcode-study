"""
给定两个字符串形式的非负整数num1 和num2，计算它们的和。

提示：
num1 和num2的长度都小于 5100
num1 和num2 都只包含数字0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            return self.addStrings(num2, num1)
        num1_arr, num2_arr = [ch for ch in num1], [ch for ch in num2]
        num1_arr.reverse()
        num2_arr.reverse()
        num_sum = [0 for _ in range(len(num2) + 1)]
        for i in range(len(num2)):
            num_sum[i] += (int(num1_arr[i] if i < len(num1) else '0') + int(num2_arr[i]))
            num_sum[i + 1] += (num_sum[i] // 10)
            num_sum[i] %= 10
        if num_sum[len(num_sum) - 1] == 0:
            del num_sum[len(num_sum) - 1]
        num_sum.reverse()
        return ''.join([str(ch) for ch in num_sum])


if __name__ == '__main__':
    assert Solution().addStrings("100", "290") == "390"
    assert Solution().addStrings("10", "290") == "300"
