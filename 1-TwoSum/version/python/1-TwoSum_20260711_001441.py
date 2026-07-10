# Last updated: 7/11/2026, 12:14:41 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen={}
4        for i,num in enumerate(nums):
5            com=target-num
6            if com in seen:
7                return [seen[com],i]
8            seen[num]=i    
9
10        