class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                if s[start] == s[end]:
                    if length <= 2 or pal[start + 1][end - 1]:
                        pal[start][end] = True

        dp = [0] * (n + 1)

        for end in range(1, n + 1):
            dp[end] = dp[end - 1]

            for start in range(end):
                if end - start >= k and pal[start][end - 1]:
                    dp[end] = max(dp[end], dp[start] + 1)

        return dp[n]