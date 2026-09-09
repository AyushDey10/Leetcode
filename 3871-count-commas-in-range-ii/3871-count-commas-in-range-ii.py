class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        x = 1000
        commas = 1

        while x <= n:
            ans += (min(n, x * 1000 - 1) - x + 1) * commas
            x *= 1000
            commas += 1

        return ans