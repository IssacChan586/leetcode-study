package com.issac.study.leetcode.simple.math;

import org.testng.Assert;
import org.testng.annotations.Test;

public class Q168 {

	@Test
	public void test() {
		Assert.assertEquals(new Solution().convertToTitle(1), "A");
		Assert.assertEquals(new Solution().convertToTitle(26), "Z");
		Assert.assertEquals(new Solution().convertToTitle(28), "AB");
		Assert.assertEquals(new Solution().convertToTitle(701), "ZY");
		Assert.assertEquals(new Solution().convertToTitle(816), "AEJ");
	}

	class Solution {
		public String convertToTitle(int n) {
			StringBuilder sb = new StringBuilder();
			while (n != 0) {
				sb.append((char) ((int) 'A' + (n - 1) % 26));
				n = (n - 1) / 26;
			}
			return sb.reverse().toString();
		}
	}

}
