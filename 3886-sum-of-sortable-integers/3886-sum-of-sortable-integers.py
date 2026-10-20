class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            good = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                wanted = target[start:start + k]

                doubled = block + block[:-1]

                # KMP prefix table for wanted
                pi = [0] * k
                j = 0

                for i in range(1, k):
                    while j > 0 and wanted[i] != wanted[j]:
                        j = pi[j - 1]
                    if wanted[i] == wanted[j]:
                        j += 1
                    pi[i] = j

                # Search wanted in the cyclic block
                j = 0
                found = False

                for x in doubled:
                    while j > 0 and x != wanted[j]:
                        j = pi[j - 1]
                    if x == wanted[j]:
                        j += 1
                    if j == k:
                        found = True
                        break

                if not found:
                    good = False
                    break

            if good:
                ans += k

        return ans