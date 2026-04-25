class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rptr=len(s)-1
        lptr=0
        for i in range(len(s)//2):
            temp=s[lptr]
            s[lptr]=s[rptr]
            s[rptr]=temp
            lptr+=1
            rptr-=1

            

        