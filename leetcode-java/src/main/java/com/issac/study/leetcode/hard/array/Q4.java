package com.issac.study.leetcode.hard.array;

import org.testng.Assert;
import org.testng.annotations.Test;

public class Q4 {

	@Test
	public void test() {
		Assert.assertEquals(new Solution().findMedianSortedArrays(new int[]{1, 3}, new int[]{2}), 2.0);
		Assert.assertEquals(new Solution().findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}), 2.5);
		Assert.assertEquals(new Solution().findMedianSortedArrays(new int[]{0, 0}, new int[]{0, 0}), 0.0);
		Assert.assertEquals(new Solution().findMedianSortedArrays(new int[]{}, new int[]{1}), 1.0);
		Assert.assertEquals(new Solution().findMedianSortedArrays(new int[]{2}, new int[]{}), 2.0);
	}

	class Solution {
		public double findMedianSortedArrays(int[] nums1, int[] nums2) {
			int totalNum = nums1.length + nums2.length;
			int nums1Point = 0, nums2Point = 0;
			int[] newArray = new int[totalNum];
			while (nums1Point < nums1.length || nums2Point < nums2.length) {
				if (nums1Point == nums1.length) {
					newArray[nums1Point + nums2Point] = nums2[nums2Point];
					nums2Point++;
				} else if (nums2Point == nums2.length) {
					newArray[nums1Point + nums2Point] = nums1[nums1Point];
					nums1Point++;
				} else {
					newArray[nums1Point + nums2Point] = Math.min(nums1[nums1Point], nums2[nums2Point]);
					if (nums1[nums1Point] < nums2[nums2Point]) {
						nums1Point++;
					} else {
						nums2Point++;
					}
				}
			}
			return totalNum % 2 == 0 ?
					(newArray[totalNum / 2 - 1] + newArray[totalNum / 2]) / 2.0 :
					newArray[totalNum / 2];
		}
	}

}
