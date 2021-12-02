class Solution:
    def calculate(self, s: str) -> int:
        #num is for converting our integer in string to easy compute
        num = 0
        sign = "+"
        stack = []
        
        # traversing thru the string plus an extra + to do final addition
        for i in (s+sign):
            # if i is digit we convert it to int
            if i.isdigit():
                #suppose we have a number without any operation so we will just convert it to proper int using this
                num = num * 10 + int(i)
                # now if our i is in operator
            elif i in "+-*/":
                # if it is + we append the stack with num that we have
                if sign == "+":
                    stack.append(num)
                # if it is - we take the num has negative
                elif sign == "-":
                    stack.append(-num)
                # now if we have multiplication suppose our s = 3 + 4 * 5, through previous iteration we appended 4 now we want to add the multiplication of it with 5 so we will pop it first and multiply it and add to stack
                elif sign == "*":
                    stack.append((stack.pop()* num))
                # similar as multiplication, popping and then dividing and adding back the result, used int to cover edge cases
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                # once traversal thru signed for next iteration we change sign to i and num to 0 so that it can reset
                sign = i
                num = 0
        #at last we return the sum of the stack
        return(sum(stack))
                
        
                
        
