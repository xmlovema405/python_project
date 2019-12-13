

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(", "}" : "{" ,"]" : "["}
        for ch in s:
            if ch in mapping:
                if stack:
                    top_element  = stack.pop()
                else:
                    top_element = "*"
                if mapping[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return not stack
