class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''The key insight: AND only keeps bits that are common 
        to all numbers in the range. As you go from left to right,
        lower bits flip between 0 and 1. Only the common prefix 
        of left and right (in binary) survives.'''
        shift=0
        while left!=right:
            left >>= 1
            right >>= 1
            shift+=1
        return left<<shift         
