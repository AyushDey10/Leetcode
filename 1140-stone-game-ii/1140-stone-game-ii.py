class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        n = len(piles)
        memo = {}

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        def solve(i, M):

            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):

                if i + X > n:
                    break

                opponent = solve(i + X, max(M, X))

                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best

            return best

        return solve(0, 1)

sol = Solution()
print(sol.stoneGameII([2,7,9,4,4]))