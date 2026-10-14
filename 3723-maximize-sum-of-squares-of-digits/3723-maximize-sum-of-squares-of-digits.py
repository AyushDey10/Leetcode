class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num:
            return ""

        ans = ""
        while num > 0:
            digit = min(9, sum)
            ans += str(digit)
            sum -= digit
            num -= 1

        return ans        