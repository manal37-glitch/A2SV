class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        mult=1
        while True:
            if mult% 2==0 and mult% n==0:
                return mult
            else:
                mult+=1
        
