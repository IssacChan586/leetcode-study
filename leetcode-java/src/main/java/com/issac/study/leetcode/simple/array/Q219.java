package com.issac.study.leetcode.simple.array;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.HashMap;
import java.util.Map;

public class Q219 {

	@Test
	public void test() {
		Assert.assertTrue(new Solution().containsNearbyDuplicate(new int[]{1, 2, 3, 1}, 3));
		Assert.assertTrue(new Solution().containsNearbyDuplicate(new int[]{1, 0, 1, 1}, 1));
		Assert.assertFalse(new Solution().containsNearbyDuplicate(new int[]{1, 2, 3, 1, 2, 3}, 2));
	}

	class Solution {
		public boolean containsNearbyDuplicate(int[] nums, int k) {
			Map<Integer, Integer> num2FirstIdx = new HashMap<>(nums.length);
			for (int i = 0; i < nums.length; i++) {
				if (num2FirstIdx.containsKey(nums[i]) && i - num2FirstIdx.get(nums[i]) <= k) {
					return true;
				}
				num2FirstIdx.put(nums[i], i);
			}
			return false;
		}
	}

}
