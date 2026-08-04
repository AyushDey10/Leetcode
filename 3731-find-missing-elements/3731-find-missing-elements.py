class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b = min(nums)
        c = max(nums)
        for i in range(b,c):
            if i in nums:
                continue
            else:
                a.append(i)
        return a

sol = Solution()
print(sol.findMissingElements([1,4,2,5]))