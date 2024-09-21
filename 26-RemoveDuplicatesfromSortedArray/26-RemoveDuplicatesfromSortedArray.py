class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):

                if nums[i]==nums[j]:
                    del nums[j]

        return len(nums)          
