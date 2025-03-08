class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num1=set(nums)
        ls1=list(num1)
        return len(nums)!=len(ls1)
        