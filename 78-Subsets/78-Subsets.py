class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out=[[]]
        for num in nums:
             out+=[cur+[num] for cur in out]

       
        return out
