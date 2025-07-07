# Last updated: 7/7/2025, 4:05:19 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
               
                
                nums[k]=nums[i]
                k+=1  
                
            
        return k
                  
            


        