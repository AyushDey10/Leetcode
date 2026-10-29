class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        timer = 0

        # Iterative DFS Euler tour
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                order.append(u)
                timer += 1
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        LOG = n.bit_length()
        up = [parent[:]]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        bit = [0] * (n + 2)

        def add(idx, val):
            idx += 1
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & -idx

        def range_xor(l, r, val):
            if l >= r:
                return
            add(l, val)
            add(r, val)

        def point_query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res

        chars = list(s)
        base = [0] * n

        for u in order:
            mask = 1 << (ord(chars[u]) - ord('a'))
            base[u] = mask ^ (base[parent[u]] if u != 0 else 0)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old = 1 << (ord(chars[u]) - ord('a'))
                new = 1 << (ord(c) - ord('a'))
                change = old ^ new

                if change:
                    range_xor(tin[u], tout[u], change)
                    chars[u] = c

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                pu = base[u] ^ point_query(tin[u])
                pv = base[v] ^ point_query(tin[v])
                pw = 1 << (ord(chars[w]) - ord('a'))

                mask = pu ^ pv ^ pw
                ans.append((mask & (mask - 1)) == 0)

        return ans