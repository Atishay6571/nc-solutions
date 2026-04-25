class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        #helper
        def isPalin(l,r):
            while l<r:
                while not s[l].isalnum() and l<r:
                    l+=1
                while not s[r].isalnum() and r>l:
                    r-=1
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while r>l and not s[r].isalnum():
                r-=1
            if s[l]!=s[r]:
                return isPalin(l+1,r) or isPalin(l,r-1)
            r-=1
            l+=1
        return True