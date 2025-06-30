# Last updated: 6/30/2025, 9:17:10 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]

        return nums    