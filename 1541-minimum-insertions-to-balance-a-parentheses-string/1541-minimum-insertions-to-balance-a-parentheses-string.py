class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        open = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                if open > 0:
                    open -= 1
                else:
                    ans += 1

            i += 1

        ans += open * 2
        return ans     