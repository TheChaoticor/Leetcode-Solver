# Last updated: 7/17/2025, 8:43:35 PM
class Solution:
    def isHappy(self, n: int) -> bool:

        seen=set()
        
        
        while n not in seen and n!=1:
            seen.add(n)
            n=sum(int(digit)**2 for digit in str(n))

        return n==1     
        