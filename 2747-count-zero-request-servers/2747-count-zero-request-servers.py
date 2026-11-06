class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda a: a[1])

        q = sorted([(queries[i], i) for i in range(len(queries))])

        count = {}
        left = 0
        right = 0
        ans = [0] * len(queries)

        for time, idx in q:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans        