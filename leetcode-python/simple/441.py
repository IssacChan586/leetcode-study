"""
你总共有n枚硬币，你需要将它们摆成一个阶梯形状，第k行就必须正好有k枚硬币。
给定一个数字n，找出可形成完整阶梯行的总行数。
n是一个非负整数，并且在32位有符号整型的范围内。

示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.

示例 2:
n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arranging-coins
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right, ans = 1, n, 1
        while left <= right:
            mid = left + (right - left) // 2
            if (1 + mid) * mid // 2 > n:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
