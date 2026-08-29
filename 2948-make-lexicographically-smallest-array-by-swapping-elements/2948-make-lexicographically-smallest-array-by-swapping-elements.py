class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)

        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        result = [0] * n
        i = 0

        while i < n:
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            values = []
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            indices.sort()

            for k in range(len(values)):
                result[indices[k]] = values[k]

            i = j + 1

        return result       