class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        prefix = stones[:]

        for i in range(1, len(stones)):
            prefix[i] += prefix[i - 1]

        ans = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans        