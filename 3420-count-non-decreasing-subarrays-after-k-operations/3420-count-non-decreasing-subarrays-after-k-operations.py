class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        nxt = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nxt[stack.pop()] = i
            stack.append(i)

        LOG = n.bit_length()
        up = [[n] * (n + 1) for _ in range(LOG)]
        sm = [[0] * (n + 1) for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]
            sm[0][i] = nums[i] * (nxt[i] - i)

        for j in range(1, LOG):
            for i in range(n):
                mid = up[j-1][i]
                up[j][i] = up[j-1][mid]
                sm[j][i] = sm[j-1][i] + sm[j-1][mid]

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def get_cost(l, r):
            p = l
            total = 0

            for j in range(LOG - 1, -1, -1):
                if up[j][p] <= r:
                    total += sm[j][p]
                    p = up[j][p]

            total += nums[p] * (r - p + 1)
            return total - (prefix[r+1] - prefix[l])

        ans = 0
        left = 0

        for right in range(n):
            while get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans
       