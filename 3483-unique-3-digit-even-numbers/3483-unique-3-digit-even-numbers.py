class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans = 0

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            x = digits[:]

            if a in x:
                x.remove(a)
            else:
                continue

            if b in x:
                x.remove(b)
            else:
                continue

            if c in x:
                x.remove(c)
            else:
                continue

            ans += 1

        return ans