class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        curr_row = 0
        direction = 1  

        for ch in s:
            rows[curr_row] += ch

            
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return "".join(rows)



sol = Solution()
print(sol.convert("PAYPALISHIRING",3))
        