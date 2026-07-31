class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        for i in range(len(digits)-1, -1, -1):
            factor= 10**i
            digit=digits[len(digits)-i-1]
            number+=(factor*digit)
        number+=1
        string= str(number)
        result=[]
        for i in string:
            result.append(int(i))
        return result