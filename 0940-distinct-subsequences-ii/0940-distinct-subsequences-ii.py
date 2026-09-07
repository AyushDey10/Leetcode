class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            total = 1
            for x in dp:
                total += x

            dp[i] = total % MOD

        return sum(dp) % MOD