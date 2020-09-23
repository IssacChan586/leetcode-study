package com.issac.study.leetcode.simple;

import org.testng.annotations.Test;

/**
 * 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
 * <p>
 * 示例 1:
 * <p>
 * 输入: "aba"
 * 输出: True
 * 示例 2:
 * <p>
 * 输入: "abca"
 * 输出: True
 * 解释: 你可以删除c字符。
 * 注意:
 * <p>
 * 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/valid-palindrome-ii
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class q680 {

	@Test
	public void test() {
		assert !new Solution().validPalindrome("eeccccbebaeeabebccceea");
		assert new Solution().validPalindrome("aba");
		assert new Solution().validPalindrome("abcddcba");
		assert new Solution().validPalindrome("abca");
		assert !new Solution().validPalindrome("aabca");
		assert new Solution().validPalindrome(
				"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga");
	}

	class Solution {
		public boolean validPalindrome(String s) {
			if (s == null || s.length() == 0) {
				return false;
			}
			for (int left = 0, right = s.length() - 1; left < right; left++, right--) {
				if (s.charAt(left) == s.charAt(right)) {
					continue;
				}
				// 删除左字符
				boolean flag1 = true, flag2 = true;
				for (int left1 = left + 1, right1 = right; left1 < right1; left1++, right1--) {
					if (s.charAt(left1) != s.charAt(right1)) {
						flag1 = false;
						break;
					}
				}
				if (flag1) {
					return true;
				}

				// 删除右字符
				for (int left1 = left, right1 = right - 1; left1 < right1; left1++, right1--) {
					if (s.charAt(left1) != s.charAt(right1)) {
						flag2 = false;
						break;
					}
				}
				return flag2;
			}
			return true;
		}
	}

	class SolutionV2 {
		public boolean validPalindrome(String s) {
			if (s == null || s.length() == 0)
				return false;
			return checkPalindrome(s, 0, s.length() - 1, false);
		}

		private boolean checkPalindrome(String s, int left, int right, boolean existDiff) {
			while (left < right) {
				if (s.charAt(left) != s.charAt(right)) {
					if (existDiff) {
						return false;
					}
					boolean flag1 = false, flag2 = false;
					if (left + 1 <= right && s.charAt(left + 1) == s.charAt(right)) {
						flag1 = checkPalindrome(s, left + 1, right, true);
					}
					if (left <= right - 1 && s.charAt(left) == s.charAt(right - 1)) {
						flag2 = checkPalindrome(s, left, right - 1, true);
					}
					return flag1 || flag2;
				}
				left++;
				right--;
			}
			return true;
		}
	}

}
