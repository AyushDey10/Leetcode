class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open = 0
        ans = 0

        for ch in s:
            if ch == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    ans += 1

        return ans + open