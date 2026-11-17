class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        # Step 1: Calculate cost for every substring
        for start in range(n):
            for end in range(start + 1, n):
                length = end - start + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):
                        count = (length - 1 - offset) // d + 1

                        for t in range(count // 2):
                            i = start + offset + t * d
                            j = start + offset + (count - 1 - t) * d

                            if s[i] != s[j]:
                                changes += 1

                    cost[start][end] = min(cost[start][end], changes)

        # Step 2: DP for exactly k partitions
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for j in range(2 * (parts - 1), i - 1):
                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]        