class Solution:
    def getSum(self, a: int, b: int) -> int:
        res=0
        carry=0
        for i in range(32):
            bitA = (a>>i) & 1
            bitB = (b>>i) & 1
            add = (bitA^bitB^carry)
            carry = (bitA & bitB) | ((bitA | bitB) & carry)
            res =  res | (add<<i)
            
        # NEW: interpret the 32-bit result as signed
        if res & (1 << 31):          # sign bit is set
            res -= (1 << 32)
        return res
