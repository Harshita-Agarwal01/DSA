# TC=0(n)+0(n)  SC=0(n)+0(n)
class Solution:
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0

    def infixToPostfix(self, s):
        # code here
        stack = []  # SC=O(n)
        result = []  # SC=O(n) bcz it is not the final ans as we join it
        for char in s:  # TC=O(n)
            if char == "(":
                stack.append(char)
            elif char.isalnum():
                result.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":  # all while loops combined= TC=O(n)
                    result.append(stack.pop())
                if stack and stack[-1] == "(":
                    stack.pop()
            else:
                while stack and stack[-1] != "(":
                    if self.precedence(char) < self.precedence(stack[-1]):
                        result.append(stack.pop())
                    elif (
                        self.precedence(char) == self.precedence(stack[-1])
                        and char != "^"
                    ):
                        result.append(stack.pop())
                    else:
                        break
                stack.append(char)
        while stack:
            result.append(stack.pop())
        return "".join(result)
