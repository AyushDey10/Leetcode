class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month - 1]) + day

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        return max(0, end - start + 1)        