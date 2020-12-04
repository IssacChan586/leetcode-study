package com.issac.study.leetcode.simple;

import org.testng.annotations.Test;

public class Q204 {

	@Test
	public void test() {
		assert new Solution().countPrimes(0) == 0;
		assert new Solution().countPrimes(1) == 0;
		assert new Solution().countPrimes(2) == 0;
		assert new Solution().countPrimes(3) == 1;
		assert new Solution().countPrimes(4) == 2;
		assert new Solution().countPrimes(10) == 4;
	}

	class Solution {
		public int countPrimes(int n) {
			if (n == 0 || n == 1) {
				return 0;
			}
			boolean[] primeFlag = new boolean[n];
			int primeCount = 0;
			for (int i = 2; i < n; i++) {
				if (!primeFlag[i]) {
					primeCount++;
					if ((long) i * i < n) {
						for (int j = i * i; j < n; j += i) {
							primeFlag[j] = true;
						}
					}
				}
			}
			return primeCount;
		}
	}

}
