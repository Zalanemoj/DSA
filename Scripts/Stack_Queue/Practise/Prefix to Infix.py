class Solution:

    def prefix_to_infix(self, string: str) -> str:
        """This function will convert given expression of prefix to in infix"""
        # Initializing empty variables
        stack = []

        # Iterating through each and every character
        for char in string[::-1]:
            # If the character is operand push it to the stack
            if char.isalnum():
                stack.append(char)
            # If the character is operator like (+,/,*,-,^)
            else:
                # Remove element from the stack and add operator between them
                operand2=stack.pop()
                operand1=stack.pop()

                # We wanted to join to operand with the operator in reverse order so that we have return operand to an operand one.
                new_exp=f"{operand2}{char}{operand1}"
                stack.append(new_exp)

        # Return the last element of the stack because it contains the full expression
        return stack[-1]

#region Printing_Solution
sol=Solution()
print(sol.prefix_to_infix("-+a*b^cde"))
#endregion