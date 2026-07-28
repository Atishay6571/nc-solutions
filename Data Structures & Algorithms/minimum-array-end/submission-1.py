class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        n -= 1  # we want the (n-1)th number after x
        bit_pos = 0
        
        while n > 0:
            # find next zero bit in x
            while result & (1 << bit_pos):
                bit_pos += 1  # skip positions where x has 1
            
            # place current bit of (n-1) into this zero position
            if n & 1:
                result |= (1 << bit_pos)
            
            n >>= 1       # next bit of n-1
            bit_pos += 1  # move to next position
        
        return result