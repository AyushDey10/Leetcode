import math

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """

        dp = [False] * (n + 1)

        for i in range(1, n + 1):

            for j in range(1, int(math.sqrt(i)) + 1):

                square = j * j

                if dp[i - square] == False:
                    dp[i] = True
                    break

        return dp[n]


sol = Solution()
print(sol.winnerSquareGame(1))