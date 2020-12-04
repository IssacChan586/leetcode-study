package com.issac.study.leetcode.medium;

import com.alibaba.fastjson.JSON;
import org.testng.annotations.Test;

public class Q34 {

	@Test
	public void test() {
		// System.out.println(JSON.toJSONString(new Solution().searchRange(new int[]{5, 7, 7, 8, 8, 10}, 8)));
		// System.out.println(JSON.toJSONString(new Solution().searchRange(new int[]{5, 7, 7, 8, 8, 10}, 6)));
		// System.out.println(JSON.toJSONString(new Solution().searchRange(new int[]{}, 0)));
		System.out.println(JSON.toJSONString(new Solution().searchRange(new int[]{1}, 1)));
	}

	class Solution {
		public int[] searchRange(int[] nums, int target) {
			/**
			 * 非二分查找
			 */
			int left = -1, right = -1;
			for (int i = 0; i < nums.length; i++) {
				if (nums[i] != target) {
					continue;
				}
				if (i == 0) {
					left = 0;
				} else if (nums[i - 1] != target) {
					left = i;
				}
				if (i == nums.length - 1) {
					right = nums.length - 1;
				} else if (nums[i + 1] != target) {
					right = i;
				}
			}
			return new int[]{left, right};
		}
	}

}
