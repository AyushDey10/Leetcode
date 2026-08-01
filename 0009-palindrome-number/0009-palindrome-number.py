class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        if a == a[::-1] :
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(121))