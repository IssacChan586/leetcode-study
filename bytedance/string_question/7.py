"""
复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "1111"
输出：["1.1.1.1"]

示例 4：
输入：s = "0(0)1(1)0(2)0(3)1(4)0(5)"
输出：["0.10.0.10","0.100.1.0"]

示例 5：
输入：s = "101(2)0(3)2(4)3(5)"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

提示：
0 <= s.length <= 3000
s 仅由数字组成
"""
from typing import List

import validator


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        len_s = len(s)
        if len_s < 4 or len_s > 12:
            return result
        for len1 in range(3):
            for len2 in range(3):
                for len3 in range(3):
                    len4 = len_s - len1 - len2 - len3 - 3
                    if len4 < 1 or len4 > 3:
                        continue
                    part1, part2, part3, part4 = s[:len1 + 1], s[len1 + 1: len1 + len2 + 2], \
                                                 s[len1 + len2 + 2: len1 + len2 + len3 + 3], s[len1 + len2 + len3 + 3:]
                    if (len(part1) > 1 and part1[0] == '0') or (len(part2) > 1 and part2[0] == '0') \
                            or (len(part3) > 1 and part3[0] == '0') or (len(part4) > 1 and part4[0] == '0'):
                        continue
                    if int(part1) <= 255 and int(part2) <= 255 and int(part3) <= 255 and int(part4) <= 255:
                        result.append('.'.join([part1, part2, part3, part4]))
        return result


if __name__ == '__main__':
    validator.validate_without_order(Solution().restoreIpAddresses("25525511135"), ["255.255.11.135", "255.255.111.35"])
    validator.validate_without_order(Solution().restoreIpAddresses("0000"), ["0.0.0.0"])
    validator.validate_without_order(Solution().restoreIpAddresses("1111"), ["1.1.1.1"])
    validator.validate_without_order(Solution().restoreIpAddresses("010010"), ["0.10.0.10", "0.100.1.0"])
    validator.validate_without_order(Solution().restoreIpAddresses("101023"),
                                     ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
