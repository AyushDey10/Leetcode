from collections import deque
class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = count
                    count += 1

        target = (1 << count) - 1

        if target == 0:
            return 0

        q = deque()
        q.append((start[0], start[1], energy, 0))

        best = {}

        best[(start[0], start[1], 0)] = energy

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        moves = 0

        while q:
            size = len(q)

            for _ in range(size):
                r, c, e, mask = q.popleft()

                if mask == target:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, nmask)

                    if ne <= best.get(state, -1):
                        continue

                    best[state] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1