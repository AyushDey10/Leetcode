class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        even = 1
        odd = 0
        total = 0
        ans = 0

        for num in arr:
            total += num

            if total % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return ans % mod        