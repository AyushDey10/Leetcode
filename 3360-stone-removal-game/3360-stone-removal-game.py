class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stones = 10
        alice = True

        while n >= stones:
            n -= stones
            stones -= 1
            alice = not alice

        return not alice