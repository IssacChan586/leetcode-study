"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z。
https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1014/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        print('min', min(strs))
        print('max', max(strs))
        for i in range(len(strs[0])):
            for s_idx in range(1, len(strs)):
                if len(strs[s_idx]) <= i or strs[0][i] != strs[s_idx][i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    assert "fl" == Solution().longestCommonPrefix(["flower", "flow", "flight"])
    assert "flower" == Solution().longestCommonPrefix(["flower", "flower", "flower"])
    assert "flower" == Solution().longestCommonPrefix(["flower", "flower1", "flower2"])
    assert "flowe" == Solution().longestCommonPrefix(["flower", "flowe", "flowe"])
    assert "" == Solution().longestCommonPrefix(["flower", "1", "flowe"])
    assert "" == Solution().longestCommonPrefix(["", "", ""])
    assert "" == Solution().longestCommonPrefix([])
