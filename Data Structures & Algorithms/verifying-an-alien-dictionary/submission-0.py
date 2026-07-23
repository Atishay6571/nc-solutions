class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        #dictionary with the neew order based on the character
        orderAlien={c:i for i,c in enumerate(order)}

        #comparing 2 adjacent pairs
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            j=0
            while j<len(w1) and j<len(w2):
                c1,c2=w1[j],w2[j]
                if (orderAlien[c1]==orderAlien[c2]):
                    j+=1
                else:
                    if (orderAlien[c1]>orderAlien[c2]):
                        return False
                    break
            if j == len(w2) and j < len(w1):  # add this
                return False                   # w1 longer, w2 is prefix
            
        else:
            return True

