class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=(str(len(s)))
            res+="@"
            res+=s

        return res
        
    def decode(self, s: str) -> List[str]:
        res=[]
        idx=0
        if s==None:
            return []
        while idx<len(s):
            lentemp=""
            while s[idx]!="@":
                lentemp+=s[idx]
                idx+=1
            
            length=int(lentemp)
            temp=""
            idx+=1
            temp=s[idx:idx+length]
            res.append(temp)
            idx+=(length)
        return res
