class Solution:

    def postfix_to_prefix(self, string: str) -> str:
        """This function will convert given expression of postfix to in prefix"""
        # Initializing empty variables
        stack = []

        # Iterating through each and every character
        for char in string:
            # If the character is operand push it to the stack
            if char.isalnum():
                stack.append(char)
            # If the character is operator like (+,/,*,-,^)
            else:
                # Remove element from the stack and add operator between them
                operand2=stack.pop()
                operand1=stack.pop()

                # Operator should be added prior to the operands
                new_exp=f"{char}{operand1}{operand2}"
                stack.append(new_exp)

        # Return the last element of the stack because it contains the full expression
        return stack[-1]

#region Printing_Solution
sol=Solution()
print(sol.postfix_to_prefix("abcd^*+e-"))
#endregion