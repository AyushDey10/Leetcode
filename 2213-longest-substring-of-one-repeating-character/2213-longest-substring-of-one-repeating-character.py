class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)

        tree = [[None, None, 0, 0, 0, 0] for _ in range(4 * n)]

        def merge(a, b):
            if a[0] is None:
                return b

            if b[0] is None:
                return a

            left_char = a[0]
            right_char = b[1]

            length = a[5] + b[5]

            prefix = a[2]
            suffix = b[3]

            if a[0] == b[0] and a[2] == a[5]:
                prefix = a[2] + b[2]

            if a[1] == b[1] and b[3] == b[5]:
                suffix = a[3] + b[3]

            best = max(a[4], b[4])

            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

            return [left_char, right_char, prefix, suffix, best, length]

        def build(node, left, right):
            if left == right:
                tree[node] = [s[left], s[left], 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(tree[1][4])

        return ans

sol = Solution()

print(sol.longestRepeating(
    "babacc",
    "bcb",
    [1, 3, 3]
))        
        