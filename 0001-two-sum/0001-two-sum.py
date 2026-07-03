class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            for jdx in range(idx + 1, len(nums)):
                if nums[idx] + nums[jdx] == target:
                    return [idx, jdx]
        return []