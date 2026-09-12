from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        n = len(intervals)

        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((r, l, w, i))

        arr.sort()

        ends = [x[0] for x in arr]
        prev = [0] * n

        for i in range(n):
            l = arr[i][1]
            prev[i] = bisect_left(ends, l)

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            r, l, w, original_index = arr[i - 1]

            for count in range(1, 5):
                skip = dp[count][i - 1]

                old_score, old_indices = dp[count - 1][prev[i - 1]]
                new_indices = tuple(sorted(old_indices + (original_index,)))
                take = (old_score + w, new_indices)

                dp[count][i] = better(skip, take)

        answer = (0, ())

        for count in range(1, 5):
            answer = better(answer, dp[count][n])

        return list(answer[1])