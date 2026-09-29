class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')':
            return False

        if (m + n - 1) % 2 == 1:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for balance in dp[i - 1][j] if i > 0 else []:
                    new_balance = balance + 1 if grid[i][j] == '(' else balance - 1
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

                for balance in dp[i][j - 1] if j > 0 else []:
                    new_balance = balance + 1 if grid[i][j] == '(' else balance - 1
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]        