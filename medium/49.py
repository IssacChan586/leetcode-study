"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        return list(ans.values())

    def groupAnagramsV2(self, strs: List[str]) -> List[List[str]]:
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

    def groupAnagramsV3(self, strs: List[str]) -> List[List[str]]:
        def get_index_key(count_map_tmp: dict):
            index_key = ''
            for ch in all_char:
                if ch not in count_map_tmp:
                    continue
                index_key = index_key + ch + str(count_map_tmp[ch])
            return index_key

        import collections
        count_maps = {}
        all_char = 'qwertyuiopasdfghjklzxcvbnm'
        for s in strs:
            index_key = get_index_key(collections.Counter(s))
            if index_key not in count_maps:
                count_maps[index_key] = []
            count_maps[index_key].append(s)
        return list(count_maps.values())

    def groupAnagramsV4(self, strs: List[str]) -> List[List[str]]:
        def get_index_key(count_map_tmp: dict):
            index_key = ''
            for ch in count_map_tmp.keys():
                index_key = index_key + '_' + ch + '_' + str(count_map_tmp[ch])
            return index_key

        count_maps = {}
        all_char = 'qwertyuiopasdfghjklzxcvbnm'
        for s in strs:
            count_map = {ch: 0 for ch in all_char}
            for j in s:
                count_map[j] += 1
            index_key = get_index_key(count_map)
            if index_key not in count_maps:
                count_maps[index_key] = []
            count_maps[index_key].append(s)
        return list(count_maps.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
