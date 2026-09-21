class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            # Subarray containing only nums[i]
            new_dp[r] += 1

            # Extend previous subarrays
            for x in range(k):
                if dp[x] > 0:
                    new_dp[(x * r) % k] += dp[x]

            dp = new_dp

            for x in range(k):
                ans[x] += dp[x]

        return ans        