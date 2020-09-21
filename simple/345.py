"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        aoeiu = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
        left, right, new_s = 0, len(s) - 1, ['' for _ in range(len(s))]
        while left <= right:
            while left < right and s[left] not in aoeiu:
                new_s[left] = s[left]
                left += 1
            while left < right and s[right] not in aoeiu:
                new_s[right] = s[right]
                right -= 1
            if left <= right:
                new_s[left], new_s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(new_s)


if __name__ == '__main__':
    assert Solution().reverseVowels("hello") == "holle"
    assert Solution().reverseVowels("helo") == "hole"
    assert Solution().reverseVowels("leetcode") == "leotcede"
