class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """

        memo = {}

        def solve(i):

            if i >= len(stoneValue):
                return 0

            if i in memo:
                return memo[i]

            take1 = stoneValue[i] - solve(i + 1)

            take2 = float("-inf")
            if i + 1 < len(stoneValue):
                take2 = stoneValue[i] + stoneValue[i + 1] - solve(i + 2)

            take3 = float("-inf")
            if i + 2 < len(stoneValue):
                take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(i + 3)

            memo[i] = max(take1, take2, take3)

            return memo[i]

        ans = solve(0)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"


sol = Solution()
print(sol.stoneGameIII([1,2,3,7]))