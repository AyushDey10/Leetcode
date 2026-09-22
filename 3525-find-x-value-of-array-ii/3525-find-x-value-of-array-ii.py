class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)

        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        def make_node(p, value):
            value %= k
            prod[p] = value
            cnt[p] = [0] * k
            cnt[p][value] = 1

        def merge(p1, p2):
            new_prod = (prod[p1] * prod[p2]) % k
            new_cnt = [0] * k

            for r in range(k):
                new_cnt[r] += cnt[p1][r]

            for r in range(k):
                nr = (prod[p1] * r) % k
                new_cnt[nr] += cnt[p2][r]

            return new_prod, new_cnt

        for i in range(n):
            make_node(size + i, nums[i])

        for i in range(size - 1, 0, -1):
            p, c = merge(i * 2, i * 2 + 1)
            prod[i] = p
            cnt[i] = c

        def update(index, value):
            p = size + index
            make_node(p, value)

            p //= 2

            while p:
                new_prod, new_cnt = merge(p * 2, p * 2 + 1)
                prod[p] = new_prod
                cnt[p] = new_cnt
                p //= 2

        def query(left, right):
            # Empty left result
            left_prod = 1
            left_cnt = [0] * k

            # Empty right result
            right_prod = 1
            right_cnt = [0] * k

            l = left + size
            r = right + size

            while l <= r:
                if l % 2 == 1:
                    old_prod = left_prod
                    new_cnt = [0] * k

                    for x in range(k):
                        new_cnt[x] += left_cnt[x]

                    for x in range(k):
                        nr = (old_prod * x) % k
                        new_cnt[nr] += cnt[l][x]

                    left_cnt = new_cnt
                    left_prod = (left_prod * prod[l]) % k
                    l += 1

                if r % 2 == 0:
                    old_prod = prod[r]
                    new_cnt = [0] * k

                    for x in range(k):
                        new_cnt[x] += cnt[r][x]

                    for x in range(k):
                        nr = (old_prod * x) % k
                        new_cnt[nr] += right_cnt[x]

                    right_cnt = new_cnt
                    right_prod = (prod[r] * right_prod) % k
                    r -= 1

                l //= 2
                r //= 2

            # left part comes before right part
            new_cnt = [0] * k

            for x in range(k):
                new_cnt[x] += left_cnt[x]

            for x in range(k):
                nr = (left_prod * x) % k
                new_cnt[nr] += right_cnt[x]

            return new_cnt

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            counts = query(start, n - 1)
            ans.append(counts[x])

        return ans     