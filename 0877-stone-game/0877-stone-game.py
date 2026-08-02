class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}

        def solve(left, right):

            if left == right:
                return piles[left]

            if (left, right) in memo:
                return memo[(left, right)]

            take_left = piles[left] - solve(left + 1, right)
            take_right = piles[right] - solve(left, right - 1)

            memo[(left, right)] = max(take_left, take_right)

            return memo[(left, right)]

        return solve(0, len(piles) - 1) >= 0
        

sol = Solution()
print(sol.stoneGame([5,3,4,5]))