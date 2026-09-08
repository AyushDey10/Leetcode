class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        if n >= 1000:
            count += n - 999

        return count