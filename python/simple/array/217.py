import collections
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(collections.Counter(nums).keys()) == len(nums)