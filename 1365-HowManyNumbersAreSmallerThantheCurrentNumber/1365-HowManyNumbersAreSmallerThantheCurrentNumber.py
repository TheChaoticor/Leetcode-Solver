class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls1=[]
        for i in range(len(nums)):
            min_c=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    min_c+=1
            ls1.append(min_c)
        return ls1    