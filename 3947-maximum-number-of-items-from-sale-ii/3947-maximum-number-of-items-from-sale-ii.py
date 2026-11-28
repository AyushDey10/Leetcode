class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1

        # M[f] = number of items whose factor is a multiple of f
        M = [0] * (n + 1)
        for f in range(1, n + 1):
            for m in range(f, n + 1, f):
                M[f] += cnt[m]

        pmin = min(p for _, p in items)
        order = sorted(items, key=lambda x: x[1])

        R = budget
        total = 0
        for f, p in order:
            if p >= 2 * pmin:
                break
            d = M[f] - 1
            if d <= 0:
                continue
            t = min(d, R // p)
            R -= t * p
            total += 2 * t
            if t < d:
                break

        total += R // pmin
        return total