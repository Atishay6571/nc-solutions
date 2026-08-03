class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # backtracking, make a choice, append answer return choose another
        result=[]
        curr=[]
        visited = set()
        def dfs(i, curr):
            if i>=len(s):
                if len(curr)==4 and tuple(curr) not in visited:
                    visited.add(tuple(curr))
                    result.append(".".join(curr))
                    return True
                return False

            for j in range(3):
                integer = s[i:i+j+1]
                if len(integer)>1 and integer[0]=="0":
                    return False
                if 0 <= int(integer) <= 255 and len(curr)<4:
                    curr.append(integer)
                    dfs(i+j+1, curr)
                    curr.pop()
                        
        dfs(0, [])
        return result

            