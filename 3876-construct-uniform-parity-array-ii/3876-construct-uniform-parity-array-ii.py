class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        if all(num % 2 == 0 for num in nums1):
            return True

        return min(nums1) % 2 == 1