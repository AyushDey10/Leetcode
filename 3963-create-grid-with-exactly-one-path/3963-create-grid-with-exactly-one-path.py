class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [["#"] * n for _ in range(m)]

        for i in range(m):
            grid[i][0] = "."

        for j in range(n):
            grid[m - 1][j] = "."

        return ["".join(row) for row in grid]        