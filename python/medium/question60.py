"""
给出集合[1,2,3,…,n]，其所有元素共有n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定n 和k，返回第k个排列。

说明：
给定 n的范围是 [1, 9]。
给定 k的范围是[1, n!]。

示例1:
输入: n = 3, k = 3
输出: "213"

示例2:
输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Todo
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 阶乘
        base_num = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        result = ""

        print(result)
        return result


if __name__ == '__main__':
    assert "213" == Solution().getPermutation(3, 3)
    assert "2314" == Solution().getPermutation(4, 9)
