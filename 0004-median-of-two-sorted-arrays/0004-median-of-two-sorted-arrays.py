class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 + nums2
        merged_array.sort()

        n = len(merged_array)

        if n % 2 == 0:
            median = (merged_array[n//2 - 1] + merged_array[n//2]) / 2.0
        else:
            median = merged_array[n//2]

        return median


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
        