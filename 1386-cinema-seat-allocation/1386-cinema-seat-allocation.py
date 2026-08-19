class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        answer = (n - len(rows)) * 2

        for row in rows:
            reserved = rows[row]

            left = 2 not in reserved and 3 not in reserved and 4 not in reserved and 5 not in reserved
            middle = 4 not in reserved and 5 not in reserved and 6 not in reserved and 7 not in reserved
            right = 6 not in reserved and 7 not in reserved and 8 not in reserved and 9 not in reserved

            if left and right:
                answer += 2

            elif left or middle or right:
                answer += 1

        return answer


sol = Solution()

print(sol.maxNumberOfFamilies(
    3,
    [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
))