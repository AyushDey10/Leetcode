class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += nums[i]
            else:
                break

        while count in nums:
            count += 1

        return count


sol = Solution()
print(sol.missingInteger([1,2,3,2,5]))