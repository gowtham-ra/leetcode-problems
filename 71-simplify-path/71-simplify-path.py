class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []        
        for ch in path:
            if ch == '' or ch == '.':
                continue
            elif ch.isalpha():
                stack.append(ch)                
            elif ch == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)


        ans = '/' + '/'.join(stack)
        
        return ans
