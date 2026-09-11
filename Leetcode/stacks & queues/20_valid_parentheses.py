# TC=O(n)  SC=O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        n = len(s)
        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                st.append(s[i])
            else:
                if st == []:
                    return False
                e = st.pop()
                if (
                    (s[i] == ")" and e == "(")
                    or (s[i] == "]" and e == "[")
                    or (s[i] == "}" and e == "{")
                ):
                    continue
                else:
                    return False
        return len(st) == 0
