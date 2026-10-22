class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def get_rotation(arr):
            k = arr.index(0)

            for j in range(n):
                if arr[(k + j) % n] != j:
                    return -1

            return k

        k = get_rotation(nums)
        if k != -1:
            return min(k, n - k + 2)

        k = get_rotation(nums[::-1])
        if k != -1:
            return 1 + min(k, n - k)

        return -1