class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(set(word))
        ans = 0

        for i in range(n):
            ans += i // 8 + 1

        return ans


sol = Solution()
print(sol.minimumPushes("abcabc"))