class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        new_tree = [[] for _ in range(n)]
        last = {}

        def dfs(node):
            ch = s[node]
            old = last.get(ch)

            if old is not None:
                new_tree[old].append(node)
            else:
                new_tree[parent[node]].append(node) if node != 0 else None

            last[ch] = node

            for child in tree[node]:
                dfs(child)

            if old is None:
                last.pop(ch)
            else:
                last[ch] = old

        dfs(0)

        ans = [0] * n

        def calc(node):
            ans[node] = 1
            for child in new_tree[node]:
                ans[node] += calc(child)
            return ans[node]

        calc(0)
        return ans
        