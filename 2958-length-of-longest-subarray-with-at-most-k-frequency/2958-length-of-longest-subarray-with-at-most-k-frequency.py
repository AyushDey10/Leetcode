class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = {}
        left = 0
        ans = 0

        for right in range(len(nums)):

            if nums[right] not in count:
                count[nums[right]] = 0

            count[nums[right]] += 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans