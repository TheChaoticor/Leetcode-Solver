# Last updated: 6/30/2025, 11:04:10 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=Counter(nums)
        for i in n.keys():
            if  n[i]==1:
                return i