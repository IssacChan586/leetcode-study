package com.issac.study.leetcode.simple.math;

import org.testng.Assert;
import org.testng.annotations.Test;

public class Q9 {

	@Test
	public void test() {
		Assert.assertEquals(new Solution().isPalindrome(1000000001), true);
		Assert.assertEquals(new Solution().isPalindrome(1342431), true);
		Assert.assertEquals(new Solution().isPalindrome(13422431), true);
		Assert.assertEquals(new Solution().isPalindrome(13423431), false);
		Assert.assertEquals(new Solution().isPalindrome(123), false);
	}

	class Solution {
		public boolean isPalindrome(int x) {
			if (x < 0) {
				return false;
			}
			String x_ = String.valueOf(x);
			int left = 0, right = x_.length() - 1;
			while (left < right) {
				if (x_.charAt(left) != x_.charAt(right)) {
					return false;
				}
				left++;
				right--;
			}
			return true;
		}
	}

}
