class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapa={}
        mapb={}
        for i in s:
            if i not in mapa:
                mapa[i]=1
            else:
                mapa[i]+=1
        for j in t:
            if j not in mapb:
                mapb[j]=1
            else:
                mapb[j]+=1
        for k in mapa:
            if k in mapb:
                if mapa[k]!=mapb[k]:
                    return False
            else:
                return False
        else:
            return True
                    