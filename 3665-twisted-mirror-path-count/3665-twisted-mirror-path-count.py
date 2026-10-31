class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def move(i, j, direction, ways):
            while 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                if direction == 0:
                    i += 1
                    direction = 1
                else:
                    j += 1
                    direction = 0

            if 0 <= i < m and 0 <= j < n:
                dp[i][j] = (dp[i][j] + ways) % MOD

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                move(i, j + 1, 0, ways)

                move(i + 1, j, 1, ways)

        return dp[m - 1][n - 1]