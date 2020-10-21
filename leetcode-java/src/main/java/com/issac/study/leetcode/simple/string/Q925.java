package com.issac.study.leetcode.simple.string;

import org.testng.Assert;
import org.testng.annotations.Test;

public class Q925 {

	@Test
	public void test() {
		Assert.assertTrue(new Solution().isLongPressedName("alex", "aaleex"));
		Assert.assertFalse(new Solution().isLongPressedName("saeed", "ssaaedd"));
		Assert.assertTrue(new Solution().isLongPressedName("leelee", "lleeelee"));
		Assert.assertTrue(new Solution().isLongPressedName("laiden", "laiden"));
		Assert.assertTrue(new Solution().isLongPressedName("", ""));
		Assert.assertTrue(new Solution().isLongPressedName("ab", "aaaaaabbb"));
		Assert.assertFalse(new Solution().isLongPressedName("ab", "aaaaaabbbc"));
		Assert.assertFalse(new Solution().isLongPressedName("aabb", "aaaaaabbbc"));
		Assert.assertTrue(new Solution().isLongPressedName("aabb", "aaaaaabbb"));
	}

	class Solution {
		public boolean isLongPressedName(String name, String typed) {
			int namePoint = 0;
			for (int typedPoint = 0; typedPoint < typed.length(); typedPoint++) {
				if (namePoint < name.length() && name.charAt(namePoint) == typed.charAt(typedPoint)) {
					namePoint++;
				} else if (namePoint == 0 || name.charAt(namePoint - 1) != typed.charAt(typedPoint)) {
					return false;
				}
			}
			return namePoint == name.length();
		}
	}

}
