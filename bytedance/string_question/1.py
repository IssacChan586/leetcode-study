"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, ch_dict, last_start_idx = 0, {}, -1
        for i, ch in enumerate(s):
            if ch in ch_dict and ch_dict[ch] > last_start_idx:
                last_start_idx = ch_dict[ch]
                ch_dict[ch] = i
            else:
                ch_dict[ch] = i
                max_len = max(max_len, i - last_start_idx)
        return max_len

    def lengthOfLongestSubstringV2(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res

    def lengthOfLongestSubstringV3(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            count_map = set()
            for j in range(i, len(s)):
                if s[j] in count_map:
                    break
                count_map.add(s[j])
            if max_len < len(count_map):
                max_len = len(count_map)
        return max_len


if __name__ == '__main__':
    assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")
    assert 1 == Solution().lengthOfLongestSubstring("bbbbb")
    assert 3 == Solution().lengthOfLongestSubstring("pwwkew")
    assert 4 == Solution().lengthOfLongestSubstring("abcd")
    assert 1 == Solution().lengthOfLongestSubstring("p")
    assert 1 == Solution().lengthOfLongestSubstring(" ")
