class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        class Fenwick:
            def __init__(self, size):
                self.bit = [0] * (size + 1)

            def add(self, i, delta):
                while i <= m:
                    self.bit[i] += delta
                    i += i & -i

            def query(self, i):
                result = 0
                while i > 0:
                    result += self.bit[i]
                    i -= i & -i
                return result

            def kth(self, target):
                idx = 0
                step = 1 << (m.bit_length() - 1)
                while step:
                    nxt = idx + step
                    if nxt <= m and self.bit[nxt] < target:
                        idx = nxt
                        target -= self.bit[nxt]
                    step >>= 1
                return idx + 1

        counts = Fenwick(m)
        sums = Fenwick(m)

        def add_value(v, delta):
            r = rank[v]
            counts.add(r, delta)
            sums.add(r, v * delta)

        def window_cost():
            median_rank = counts.kth((x + 1) // 2)
            median = vals[median_rank - 1]

            left_count = counts.query(median_rank)
            left_sum = sums.query(median_rank)

            total_sum = sums.query(m)
            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        costs = []
        for i in range(x):
            add_value(nums[i], 1)
        costs.append(window_cost())

        for start in range(1, n - x + 1):
            add_value(nums[start - 1], -1)
            add_value(nums[start + x - 1], 1)
            costs.append(window_cost())

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x and prev[i - x] != INF:
                    cost = costs[i - x]
                    curr[i] = min(curr[i],
                                  prev[i - x] + cost)

            prev = curr

        return prev[n]        