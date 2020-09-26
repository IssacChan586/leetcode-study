"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-only-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s_list, left, right = list(S), 0, len(S) - 1
        while left < right:
            if not str.isalpha(s_list[left]):
                left += 1
            if not str.isalpha(s_list[right]):
                right -= 1
            if str.isalpha(s_list[left]) and str.isalpha(s_list[right]):
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return ''.join(s_list)

    def reverseOnlyLettersV3(self, S: str) -> str:
        letters, ans = [c for c in S if c.isalpha()], []
        for ch in S:
            if ch.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(ch)
        return ''.join(ans)

    def reverseOnlyLettersV2(self, S: str) -> str:
        s_list, left, right = list(S), 0, len(S) - 1
        while left < right:
            while left < right and not str.isalpha(s_list[left]):
                left += 1
            while left < right and not str.isalpha(s_list[right]):
                right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ''.join(s_list)


if __name__ == '__main__':
    assert Solution().reverseOnlyLetters("ab-cd") == "dc-ba"
    assert Solution().reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
