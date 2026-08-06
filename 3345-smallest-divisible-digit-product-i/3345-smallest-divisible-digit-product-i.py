class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """

        while True:

            a = str(n)
            b = 1

            for i in a:
                b *= int(i)

            if b % t == 0:
                return n

            n += 1


sol = Solution()
print(sol.smallestNumber(10, 2))