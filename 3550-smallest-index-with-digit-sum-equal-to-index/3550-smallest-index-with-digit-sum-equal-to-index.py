class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []

        for i, num in enumerate(nums):
            b = 0

            for j in str(num):
                b += int(j)

            if i == b:
                a.append(i)

        if a:
            return min(a)
        return -1
