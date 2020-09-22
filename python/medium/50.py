"""
实现pow(x, n)，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例2:
输入: 2.10000, 3
输出: 9.26100

示例3:
输入: 2.00000, -2
输出: 0.25000
解释: 2^(-2) = 1 / 2^2 = 1/4 = 0.25

说明:
-100.0 <x< 100.0
n 是 32 位有符号整数，其数值范围是[−2^31,2^31 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from python.validator import validate


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPowV2(self, x: float, n: int) -> float:
        return round(pow(x, n), 5)


if __name__ == '__main__':
    validate(Solution().myPow(2.00000, 10), 1024.00000)
    validate(Solution().myPow(2.10000, 3), 9.26100)
    validate(Solution().myPow(2.00000, -2), 0.25000)
