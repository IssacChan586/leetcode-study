"""
我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。
例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。

示例 1：
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。

示例 2：
输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。

提示：
1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] 都是小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            return s.count(min(list(s)))

        word_count = {i: 0 for i in range(11)}
        for word_tmp in [f(word) for word in words]:
            word_count[word_tmp] += 1
        word_sum = [0] * 12
        for i in range(10, 0, -1):
            word_sum[i] = word_sum[i + 1] + word_count[i]
        return [word_sum[f(query) + 1] for query in queries]

    def numSmallerByFrequencyV2(self, queries: List[str], words: List[str]) -> List[int]:
        import collections

        def f(s: str) -> int:
            all_char = 'abcdefghijklmnopqrstuvwxyz'
            tmp_count = collections.Counter(s)
            for ch in all_char:
                if ch in tmp_count:
                    return tmp_count[ch]

        word_ans = [f(word) for word in words]
        word_ans.sort()
        ans = []
        for query in queries:
            f_query = f(query)
            ans.append(0)
            for i in range(len(word_ans)):
                if f_query < word_ans[i]:
                    ans[len(ans) - 1] = len(word_ans) - i
                    break
        return ans


if __name__ == '__main__':
    assert Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]) == [1, 2]
    assert Solution().numSmallerByFrequency(
        ["aabbabbb", "abbbabaa", "aabbbabaa", "aabba", "abb", "a", "ba", "aa", "ba", "baabbbaaaa", "babaa", "bbbbabaa"],
        ["b", "aaaba", "aaaabba", "aa", "aabaabab", "aabbaaabbb", "ababb", "bbb", "aabbbabb", "aab", "bbaaababba",
         "baaaaa"]) == [6, 5, 0, 6, 11, 11, 11, 8, 11, 0, 6, 6]
    assert Solution().numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]) == [1]
