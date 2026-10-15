class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                ans += len(seen) * len(seen)

        return ans        