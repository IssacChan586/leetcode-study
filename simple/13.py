"""
罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

示例1:
输入:"III"
输出: 3

示例2:
输入:"IV"
输出: 4

示例3:
输入:"IX"
输出: 9

示例4:
输入:"LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例5:
输入:"MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.


提示：
题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IC 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def romanToInt(self, s: str) -> int:
        len_s, left, result = len(s), 0, 0
        ch_2_count = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                      ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        for pair in ch_2_count:
            len_pair = len(pair[0])
            while left + len_pair <= len(s) and s[left:left + len_pair] == pair[0]:
                result += pair[1]
                left = left + len_pair
        return result

    def romanToIntV2(self, s: str) -> int:
        roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        str_lenth = len(s)
        res = 0
        for i in range(str_lenth):
            if i < str_lenth - 1 and roman_dic[s[i]] < roman_dic[s[i + 1]]:
                res -= roman_dic[s[i]]
            else:
                res += roman_dic[s[i]]
        return res

    def romanToIntV3(self, s: str) -> int:
        result = 0
        ch_2_count = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                      ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        for pair in ch_2_count:
            while s.startswith(pair[0]):
                result += pair[1]
                s = s[len(pair[0]):]
        return result

    def romanToIntV4(self, s: str) -> int:
        result = 0
        ch_2_count = [['CM', 900], ['M', 1000], ['CD', 400], ['D', 500], ['XC', 90], ['C', 100], ['XL', 40], ['L', 50],
                      ['IX', 9], ['X', 10], ['IV', 4], ['V', 5], ['I', 1]]
        while len(s) != 0:
            for pair in ch_2_count:
                if s.startswith(pair[0]):
                    result += pair[1]
                    s = s[len(pair[0]):]
                    break
        return result


if __name__ == '__main__':
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
