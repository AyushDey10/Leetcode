class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        qdiff = left_q - right_q
        diff = left_sum - right_sum

        if qdiff % 2 != 0:
            return True

        return diff != -9 * qdiff // 2