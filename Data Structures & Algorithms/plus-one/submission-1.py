class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry=1
        for i in range(len(digits)):
            new = digits[i]+carry
            if new<=9:
                digits[i]=new
                carry=0
                break
            else:
                digits[i]=new%10
                carry=1
        if carry:
            digits.append(1)
        return digits[::-1]                
