class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxv=max(candies)
        outb=[]
        for i in range(len(candies)):
            sum=candies[i]+extraCandies
            if maxv<=sum:
               
                outb.append(True)
            else:
                outb.append(False)    
             
        return outb
