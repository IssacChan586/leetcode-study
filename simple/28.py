class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1

    def strStrV2(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().strStr('', '') == 0
    assert Solution().strStr('a', 'a') == 0
    assert Solution().strStr('hello', 'll') == 2
    assert Solution().strStr('hello', 'ww') == -1
