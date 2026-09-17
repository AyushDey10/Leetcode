class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        best = [n + 1] * (n + 1)

        left = 0
        total = 0
        ans = n + 1

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if best[left] != n + 1:
                    ans = min(ans, length + best[left])

                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        if ans == n + 1:
            return -1

        return ans