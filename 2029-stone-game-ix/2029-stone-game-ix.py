class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        if count[0] % 2 == 1:
            return abs(count[1] - count[2]) > 2
        else:
            return count[1] > 0 and count[2] > 0

sol = Solution()
print(sol.stoneGameIX([2,1]))