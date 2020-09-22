"""
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写，比如"Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:
输入: "USA"
输出: True

示例 2:
输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-capital
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag1, flag2, flag3 = True, True, True
        for idx in range(len(word)):
            is_upper_case = word[idx].isupper()
            if flag1 and not is_upper_case:
                # 全部字母都是大写，比如"USA"
                flag1 = False
            if flag2 and is_upper_case:
                # 单词中所有字母都不是大写，比如"leetcode"
                flag2 = False
            if flag3 and idx > 0 and is_upper_case:
                # 如果单词不只含有一个字母，只有首字母大写，比如"Google"
                flag3 = False
        return flag1 or flag2 or flag3


if __name__ == '__main__':
    assert Solution().detectCapitalUse("USA")
    assert not Solution().detectCapitalUse("FlaG")
    assert Solution().detectCapitalUse("Flag")
    assert Solution().detectCapitalUse("flag")
