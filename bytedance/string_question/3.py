"""
字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

http://pallas-staging.vip.vip.com/#/cluster_detail?clusterId=pallas-staging-vm
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding windows
        from collections import Counter
        count_s1, chars_needed = Counter(s1), len(s1)
        left, right = 0, 0
        while right < len(s2):
            r_c = s2[right]
            if r_c in count_s1:
                if count_s1[r_c] > 0:
                    chars_needed -= 1
                count_s1[r_c] -= 1

            while chars_needed == 0:
                if right - left + 1 == len(s1):
                    return True
                l_c = s2[left]
                if l_c in count_s1:
                    count_s1[l_c] += 1
                    if count_s1[l_c] > 0:
                        chars_needed += 1
                left += 1
            right += 1
        return False

    def checkInclusionV3(self, s1: str, s2: str) -> bool:
        len_s1, len_s2, count_s1, count_s2 = len(s1), len(s2), {}, {}
        if len_s1 > len_s2:
            return False
        for i in "abcdefghijklmnopqrstuvwxyz":
            count_s1[i], count_s2[i] = 0, 0
        for i in range(len_s1):
            count_s1[s1[i]] += 1
            count_s2[s2[i]] += 1
        for i in range(len_s1, len_s2):
            if count_s1 == count_s2:
                return True
            count_s2[s2[i - len_s1]] -= 1
            count_s2[s2[i]] += 1
        return count_s1 == count_s2

    def checkInclusionV2(self, s1: str, s2: str) -> bool:
        count_s1, count_s2, left_idx, len_s1, cur_len_s2 = {i: s1.count(i) for i in s1}, {}, 0, len(s1), 0
        for s in s2:
            cur_len_s2 += 1
            if len_s1 >= cur_len_s2:
                count_s2[s] = count_s2[s] + 1 if s in count_s2 else 1
            else:
                if count_s2[s2[left_idx]] == 1:
                    del count_s2[s2[left_idx]]
                else:
                    count_s2[s2[left_idx]] -= 1
                count_s2[s] = count_s2[s] + 1 if s in count_s2 else 1
                left_idx += 1
            if count_s1 == count_s2:
                return True
        return False


if __name__ == '__main__':
    assert not Solution().checkInclusion("ab", "a")
    assert Solution().checkInclusion("ab", "abc")
    assert Solution().checkInclusion("ab", "eidbaooo")
    assert not Solution().checkInclusion("ab", "eidboaoo")
    assert Solution().checkInclusion("abcaab", "eidbabcaaboaoo")
