# Last updated: 7/18/2025, 9:10:46 PM
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n=Counter(nums)
        sorg=sorted(n.items(),key=lambda x: x[1],reverse=True)

        result=[item[0] for item in sorg]
        return result[:k]
        
        