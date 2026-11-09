import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        busy = []
        count = [0] * k

        available = list(range(k))
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(pos, val):
            pos += size
            tree[pos] = val
            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(start):
            def search(node, left, right):
                if right <= start or tree[node] == 0:
                    return -1

                if right - left == 1:
                    return left

                mid = (left + right) // 2

                res = search(2 * node, left, mid)
                if res != -1:
                    return res

                return search(2 * node + 1, mid, right)

            return search(1, 0, size)

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            server = find_first(i % k)

            if server == -1:
                server = find_first(0)

            if server == -1:
                continue

            count[server] += 1
            update(server, 0)

            heapq.heappush(busy, (arrival[i] + load[i], server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]        