# 1. If brackets doesn't match -> False
# 2. At the end stack is not empty -> False
# 3. If you find closing , but stack is empty -> False

class Solution:

    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
            # If there is one any opening bracket then append in the uh stack
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else: # The health condition deals with the closing brackets
                #  If there is a closing bracket but the stack does not contain opening bracket then return false
                if len(stack) == 0:
                    return False
                # Popping out and comparing in order to check for valid parentheses
                ch=stack.pop()
                if ((char == ')' and ch == '(')
                    or (char == ']' and ch == '[') or (char == '}' and ch == '{')):
                    continue
                else: # If no Valid parentheses
                    return False
        return len(stack) == 0 # If len(stack) == 0 then return True otherwise False

sol=Solution()                      # Making an object of the class solution
print(sol.is_valid("(())"))         # Printing out valid or in valid