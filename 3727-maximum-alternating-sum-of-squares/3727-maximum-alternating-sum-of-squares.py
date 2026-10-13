class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(x * x for x in nums)
        n = len(nums)
        return sum(nums[n // 2:]) - sum(nums[:n // 2])        