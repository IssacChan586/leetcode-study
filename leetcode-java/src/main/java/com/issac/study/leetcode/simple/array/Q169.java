package com.issac.study.leetcode.simple.array;

import org.testng.Assert;
import org.testng.annotations.Test;

public class Q169 {

	@Test
	public void test() {
		Assert.assertEquals(new Solution().majorityElement(new int[]{3, 2, 3}), 3);
		Assert.assertEquals(new Solution().majorityElement(new int[]{2, 2, 1, 1, 1, 2, 2}), 2);
	}

	class Solution {
		/**
		 * Boyer Moore Voting Algorithm
		 * @param nums
		 * @return
		 */
		public int majorityElement(int[] nums) {
			int majorNum = nums[0], count = 0;
			for (int num : nums) {
				majorNum = count == 0 ? num : majorNum;
				count += (num == majorNum ? 1 : -1);
			}
			return majorNum;
		}
	}

}
