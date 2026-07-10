# Last updated: 7/10/2026, 11:58:41 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        for i in range(0,len(nums)):
4            for j in range(0, len(nums)):
5                if i!=j and nums[i]+nums[j]==target:
6                    return [i,j]
7
8
9        