# Last updated: 6/21/2025, 10:04:13 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst=[]
        num=Counter(nums)
        l=0
        num=sorted(num.items(),key=lambda item: item[1],reverse=True)
        
        
        return [item[0] for item in num[:k]]


        