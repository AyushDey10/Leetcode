class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        ans = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                count = 0

                for i in range(n):
                    for j in range(n):
                        ni = i + dr
                        nj = j + dc

                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                count += 1

                ans = max(ans, count)

        return ans