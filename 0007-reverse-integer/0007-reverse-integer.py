class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            a = ""
            for i in str(x):
                a +=i
                b = int(a[::-1])
        else:
            y = abs(x)
            a = ""
            for i in str(y):
                a+=i
                b = -int(a[::-1])
        
        if b < -2**31 or b > 2**31 -1:
            return 0
            
        return b


sol = Solution()
print(sol.reverse(123))