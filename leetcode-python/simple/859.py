"""
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

示例 1：
输入： A = "ab", B = "ba"
输出： true

示例 2：
输入： A = "ab", B = "ab"
输出： false

示例 3:
输入： A = "aa", B = "aa"
输出： true

示例 4：
输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

示例 5：
输入： A = "", B = "aa"
输出： false
 
提示：
0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        import collections
        len_a, len_b = len(A), len(B)
        if len_a != len_b:
            return False
        if A == B:
            count_a = collections.Counter(A)
            for ch in count_a.keys():
                if count_a[ch] > 1:
                    return True
        diff_count, first_diff_ch_a, first_diff_ch_b = 0, '', ''
        for i in range(len_a):
            if A[i] != B[i]:
                if diff_count == 0:
                    first_diff_ch_a, first_diff_ch_b = A[i], B[i]
                elif diff_count == 1:
                    if first_diff_ch_a != B[i] or first_diff_ch_b != A[i]:
                        return False
                else:
                    return False
                diff_count += 1
        return diff_count == 2


if __name__ == '__main__':
    assert Solution().buddyStrings("ab", "ba")
    assert Solution().buddyStrings("aaaaaaabc", "aaaaaaacb")
    assert Solution().buddyStrings("aa", "aa")
    assert Solution().buddyStrings("aabb", "aabb")
    assert not Solution().buddyStrings("ab", "ab")
