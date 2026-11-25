class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        BASE = 100003

        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            prefix[i + 1] = (prefix[i] * BASE + nums[i]) % MOD
            power[i + 1] = (power[i] * BASE) % MOD

        def check(k):
            count = {}

            for i in range(n - k + 1):
                h = (prefix[i + k] - prefix[i] * power[k]) % MOD
                count[h] = count.get(h, 0) + 1

            return any(v == 1 for v in count.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left