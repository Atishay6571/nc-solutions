class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        result=""
        answer=""
        path+='/'
        for i in path:
            if i in {'/'}:
                if result=='..':
                    if len(stack)!=0:                    
                        stack.pop()
                    result="" 
                elif result==".":
                    result=""
                elif len(result)!=0:
                    stack.append(result)
                    result=""
            else:
                result+=i
        stack.append(result)
        while stack:
            val=stack.pop(0)
            answer+='/'
            answer+=val
        if answer[-1]=='/' and len(answer)>1:
            answer=answer[:-1:]
        return answer
        


