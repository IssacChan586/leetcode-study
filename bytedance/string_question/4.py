"""
字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # 进行反转以方便进位, 如 "123" 倒转成 ["3", "2", "1"]
        num1_arr = [int(num1[len(num1) - i - 1]) for i in range(len(num1))]
        num2_arr = [int(num2[len(num2) - i - 1]) for i in range(len(num2))]

        sum_arr = [0 for _ in range(len(num1) + len(num2) + 1)]
        for i in range(len(num1)):
            for j in range(len(num2)):
                sum_arr[i + j] = sum_arr[i + j] + num1_arr[i] * num2_arr[j]

        for i in range(len(sum_arr)):
            if sum_arr[i] >= 10:
                sum_arr[i + 1] = sum_arr[i + 1] + int(sum_arr[i] / 10)
                sum_arr[i] = sum_arr[i] % 10

        while sum_arr[len(sum_arr) - 1] == 0:
            sum_arr.pop(len(sum_arr) - 1)
        sum_arr.reverse()
        return ''.join(str(i) for i in sum_arr)


if __name__ == '__main__':
    assert Solution().multiply("0", "3") == "0"
    assert Solution().multiply("123", "456") == "56088"
    assert Solution().multiply("2", "3") == "6"
    assert Solution().multiply("999", "999") == "998001"
    assert Solution().multiply("5", "12") == "60"
