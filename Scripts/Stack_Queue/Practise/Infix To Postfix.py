class Solution:
    def priority(self,character : str)->int:
        """And this function will provide that which variable is given which priority"""
        if character in ["+", "-"]:
            return 1
        if character in ["*","/"]:
            return 2
        if character == "^":
            return 3
        return 0

    def infix_to_postfix(self,string : str)->str:
        """This function will convert infix to postfix"""

        # Initializing empty list
        stack = []
        result=[]

        # Running a for loop for iterating over all character
        for char in string:
            # If it is a variable then don't do anything just appended to the result
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            # If Character is "(" append to the Stack
            elif char == "(":
                stack.append(char)
            # If Character is ")" Remove all elements and append to the result up till that character
            elif char == ")":
                while len(stack)>0 and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # For removal of ")" parentheses
            #  Adding operate turn to the result if it has greater priority
            else:
                while len(stack)>0 and self.priority(stack[-1]) >= self.priority(char):
                    result.append(stack.pop())
                stack.append(char)
        # Adding remaining elements to result
        while stack:
            result.append(stack.pop())

        # Returning result by converting it to String
        return "".join(result)

# region Printing_Solution
sol=Solution()

print(sol.infix_to_postfix("a+b*(c^d)-e"))
# endregion

# abcd^*+e-