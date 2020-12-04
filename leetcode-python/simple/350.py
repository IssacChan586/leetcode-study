"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果nums1的大小比nums2小很多，哪种方法更优？
如果nums2的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List

from validator import validate_without_order


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = collections.Counter(nums1)
        result = []
        for i in range(len(nums2)):
            if nums1_count.get(nums2[i], 0) > 0:
                result.append(nums2[i])
                nums1_count[nums2[i]] -= 1
        return result

    def intersectV2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        result = []
        for i in range(len(nums1)):
            if not nums2:
                break
            if nums1[i] in nums2:
                result.append(nums1[i])
                nums2.remove(nums1[i])
        return result


if __name__ == '__main__':
    validate_without_order(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
    validate_without_order(Solution().intersect([1, 2, 2, 1], [2, 2]), [2, 2])
