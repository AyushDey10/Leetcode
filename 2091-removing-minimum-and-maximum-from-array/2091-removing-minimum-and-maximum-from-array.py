class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        a = nums.index(min(nums))
        b = nums.index(max(nums))

        if a > b:
            a, b = b, a

        x = b + 1
        y = n - a
        z = (a + 1) + (n - b)

        return min(x, y, z)