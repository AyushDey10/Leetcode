class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

    
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return

            suspicious.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans


sol = Solution()

print(sol.remainingMethods(
    4,
    1,
    [[1,2],[0,1],[3,2]]
))
