class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #creating a stack to keep track of index number for open parenthesis
        stack = []
        N = len(s)
        #converting string to list so that popping is easier
        S = list(s)
        for i in range(N):
            if S[i] == "(":
                #if open parenthesis we storing the value of i
                stack.append(i)
            elif S[i] == ")":
                #if we have stack we open parenthesis value we will pop the index as it is valid parenthesis
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
            
        for j in stack:
            S[j] = ""
        return "".join(S)
        