class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def update(node, start, end, l, r):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                length = end - start + 1
                tree[node] += 2 * lazy[node] * 0
                apply(node, start, end, 1)
                return

            mid = (start + end) // 2
            push(node, start, end)
            update(node * 2, start, mid, l, r)
            update(node * 2 + 1, mid + 1, end, l, r)
            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

        def apply(node, start, end, val):
            length = end - start + 1
            tree[node] = (tree[node] + 2 * val * sums[node] + val * val * length) % MOD
            sums[node] = (sums[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, start, end):
            if lazy[node] != 0 and start != end:
                mid = (start + end) // 2
                apply(node * 2, start, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, end, lazy[node])
                lazy[node] = 0

        sums = [0] * (4 * n)

        def range_add(node, start, end, l, r):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                apply(node, start, end, 1)
                return
            mid = (start + end) // 2
            push(node, start, end)
            range_add(node * 2, start, mid, l, r)
            range_add(node * 2 + 1, mid + 1, end, l, r)
            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD
            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            range_add(1, 0, n - 1, left, i)
            last[x] = i
            ans = (ans + tree[1]) % MOD

        return ans