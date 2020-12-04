class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        prime_flag = [False for _ in range(n)]
        prime_count = 0
        for i in range(2, n):
            if not prime_flag[i]:
                prime_count += 1
                if i * i < n:
                    for j in range(i * i, n, i):
                        prime_flag[j] = True
        return prime_count


if __name__ == '__main__':
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(0) == 0
