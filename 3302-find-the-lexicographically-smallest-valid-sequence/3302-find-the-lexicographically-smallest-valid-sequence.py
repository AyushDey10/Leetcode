class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n = len(word1)
        m = len(word2)

        suffix = [0] * (n + 1)

        j = m - 1
        count = 0

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
                count += 1

            suffix[i] = count

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not changed:
                remaining = m - j - 1

                if suffix[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    changed = True

        if j == m:
            return ans

        return []

sol = Solution()
print(sol.validSequence("vbcca", "abc"))