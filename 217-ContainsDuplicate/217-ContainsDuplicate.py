class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ls1=sum(nums)
        n=len(nums)
        sum1=(n*(n+1))//2
        return sum1-ls1