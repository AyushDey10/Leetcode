class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        memo = {}

        def solve(left, right):
            if left == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            ans = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for i in range(left, right):
                left_sum += stoneValue[i]
                right_sum -= stoneValue[i]

                if left_sum < right_sum:

                    if ans >= left_sum * 2:
                        continue

                    ans = max(ans, left_sum + solve(left, i))

                elif left_sum > right_sum:

                    if ans >= right_sum * 2:
                        break

                    ans = max(ans, right_sum + solve(i + 1, right))

                else:

                    ans = max(
                        ans,
                        left_sum + solve(left, i),
                        right_sum + solve(i + 1, right)
                    )

            memo[(left, right)] = ans
            return ans

        return solve(0, n - 1)


sol = Solution()
print(sol.stoneGameV([6, 2, 3, 4, 5, 5]))