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
        stack = []
        result = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char.isalnum():
                result.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
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
