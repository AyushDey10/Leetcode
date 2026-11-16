class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = 0

                for digit in group:
                    total += int(digit)

                new_s += str(total)

            s = new_s

        return s        