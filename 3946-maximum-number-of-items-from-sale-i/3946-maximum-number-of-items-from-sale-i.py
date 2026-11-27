class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)

        freq = [0] * 1501
        for f, p in items:
            freq[f] += 1

        groups = [[] for _ in range(1501)]

        for f, p in items:
            free = sum(freq[x] for x in range(f, 1501, f)) - 1
            groups[p].append((p, free + 1))

        dp = [0] * (budget + 1)
        ans = 0

        for p in range(1500, 0, -1):
            if not groups[p]:
                continue

            # Subsets containing at least one item costing p
            cur = [-1] * (budget + 1)

            for cost, value in groups[p]:
                for b in range(budget, cost - 1, -1):
                    if dp[b - cost] != -1:
                        cur[b] = max(cur[b], dp[b - cost] + value)

                    if cur[b - cost] != -1:
                        cur[b] = max(cur[b], cur[b - cost] + value)

            for b in range(budget + 1):
                if cur[b] != -1:
                    ans = max(ans, cur[b] + (budget - b) // p)

            # Add this price group to the general DP
            for cost, value in groups[p]:
                for b in range(budget, cost - 1, -1):
                    dp[b] = max(dp[b], dp[b - cost] + value)

        return ans