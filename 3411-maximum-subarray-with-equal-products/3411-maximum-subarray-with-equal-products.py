import math

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ans = 0
        n = len(nums)

        for i in range(n):
            product = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                product *= x
                g = gcd(g, x)
                l = (l * x) // gcd(l, x)

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans