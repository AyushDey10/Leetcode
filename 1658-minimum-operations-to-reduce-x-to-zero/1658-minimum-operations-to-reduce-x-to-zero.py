class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1

        left = 0
        curr = 0
        longest = -1

        for right in range(n):
            curr += nums[right]

            while curr > target and left <= right:
                curr -= nums[left]
                left += 1

            if curr == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return n - longest        