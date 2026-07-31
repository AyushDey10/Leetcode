class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """


        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] == "+":
            sign = 1
            i = 1
        elif s[0] == "-":
            sign = -1
            i = 1

        digit = ""

        while i < len(s) and s[i].isdigit():
            digit += s[i]
            i += 1

        if digit == "":
            return 0

        a = 0
        for ch in digit:
            a = a * 10 + (ord(ch) - ord('0'))

        a *= sign

        if a > 2**31 - 1:
            return 2**31 - 1

        if a < -2**31:
            return -2**31

        return a


sol = Solution()
print(sol.myAtoi("42"))