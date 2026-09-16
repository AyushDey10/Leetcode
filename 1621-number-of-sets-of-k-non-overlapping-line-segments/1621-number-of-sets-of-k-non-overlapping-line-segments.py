class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 1000000007

        a = 1
        b = 1

        for i in range(1, 2 * k + 1):
            a = a * (n + k - i) % MOD
            b = b * i % MOD

        return a * pow(b, MOD - 2, MOD) % MOD