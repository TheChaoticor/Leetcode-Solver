# Last updated: 5/21/2025, 8:42:43 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[0]*len(nums)
        kl=math.prod(nums)
        for i in range(len(nums)):
            answer[i]=int(kl/nums[i]) if nums[i]!=0 else math.prod(nums[0:i])*math.prod(nums[i+1:len(nums)])
        return answer
            