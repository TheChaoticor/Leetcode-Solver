# Last updated: 7/18/2025, 7:30:40 PM
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if k==0 or not nums:
            return []
        minheap=nums[:k]
        heapq.heapify(minheap)
        for num in nums[k:]:
            if num>minheap[0]:
                heapq.heappushpop(minheap,num)

        return minheap[0]       
