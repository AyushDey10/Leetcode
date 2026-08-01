class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def solve(left, right):
            if left == right:
                return nums[left]

            take_left = nums[left] - solve(left + 1, right)
            take_right = nums[right] - solve(left, right - 1)

            return max(take_left, take_right)

        return solve(0, len(nums) - 1) >= 0

sol = Solution()
print(sol.predictTheWinner([1,5,2]))