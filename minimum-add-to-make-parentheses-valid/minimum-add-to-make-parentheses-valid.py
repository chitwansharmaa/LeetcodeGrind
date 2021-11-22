class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c = 0
        S = list(s)
        N = len(s)
        for i in range(N):
            if S[i] == "(":
                stack.append(S[i])
            else:
                if len(stack)  and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(S[i])
            
                    
        return(len(stack))
                    
        
            
                
            
        