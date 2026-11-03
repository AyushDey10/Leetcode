class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = max(nums)
        return sum(target - x for x in nums)        