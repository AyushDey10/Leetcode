class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """

        add = 0
        product = 1

        for i in str(n):
            add += int(i)

        for i in str(n):
            product *= int(i)

        total = add + product

        return n % total == 0


sol = Solution()
print(sol.checkDivisibility(99))   # True