class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2
            need = sum(max(0, x - mid) for x in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        ans = 0
        remaining = k

        for x in diff:
            reduction = max(0, x - left)
            remaining -= reduction
            ans += min(x, left) ** 2

        for x in diff:
            if remaining > 0 and x >= left and x > 0:
                ans -= left * left - (left - 1) * (left - 1)
                remaining -= 1

        return ans