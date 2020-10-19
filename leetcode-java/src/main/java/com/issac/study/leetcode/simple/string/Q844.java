package com.issac.study.leetcode.simple.string;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.Arrays;

public class Q844 {

	@Test
	public void test() {
		Assert.assertTrue(new Solution().backspaceCompare("123", "123"));
		Assert.assertTrue(new Solution().backspaceCompare("123", "1234#"));
		Assert.assertTrue(new Solution().backspaceCompare("123#####", "1234#######"));
	}

	class Solution {
		private String backspace(String str) {
			int strPoint = 0;
			char[] newStr = new char[str.length()];
			for (int i = 0; i < str.length(); i++) {
				if (str.charAt(i) == '#') {
					strPoint = Math.max(0, strPoint - 1);
				} else {
					newStr[strPoint++] = str.charAt(i);
				}
			}
			return new String(Arrays.copyOf(newStr, strPoint));
		}

		public boolean backspaceCompare(String S, String T) {
			return backspace(S).equals(backspace(T));
		}
	}

}
