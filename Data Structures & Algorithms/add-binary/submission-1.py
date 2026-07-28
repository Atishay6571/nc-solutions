class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        res=""
        carry=0
        i,j=0,0
        while i<len(a) and j<len(b):
            res+= str(int(a[i])^int(b[j])^carry)
            carry= (int(a[i])&int(b[j])) | ((int(a[i])|int(b[j]))&carry)
            i+=1
            j+=1
        while i<len(a):
            res+=str(int(a[i]) ^ carry)
            carry &= int(a[i])
            i+=1
        while j<len(b):
            res+=str(int(b[j]) ^ carry)
            carry &= int(b[j])
            j+=1
        if carry:
            res+="1"
        return res[::-1]

            