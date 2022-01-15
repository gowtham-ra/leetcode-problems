class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        :type input: str
        :rtype: List[int]
        """        
        def ways(input, memo):
            if input.isdigit():
                return [int(input)]
            if input in memo:
                return memo[input] 
            res = []
            for i in range(len(input)):
                if input[i] in "-+*":
                    l = self.diffWaysToCompute(input[:i])
                    r = self.diffWaysToCompute(input[i+1:])
                    for j in l:
                        for k in r:
                            res.append(self.helper(j, k, input[i]))
            memo[input] = res
            
            return res
        
        return ways(expression, {})


    def helper(self, op1, op2, op):
        if op == "+":
            return op1+op2
        elif op == "-":
            return op1-op2
        else:
            return op1*op2

"""
      
        
        answer = []
        dp = {}
        return self.ways(expression, m)
    
    def ways(self, expression, m):
        if expression.isdigit():
            return [int(expression)]
        if expression in m:
            return m[expression]
        
        for i in range(len(expression)):
            ch = expression[i]
            
            if not ch.isdigit:
                l = expression[0:i]
                r = expression[i+1:]
                
                left = self.diffWaysToCompute(l)
                right = self.diffWaysToCompute(r)
                
                for op1 in left:
                    for op2 in right:
                        answer.append(self.operation(op1, op2, ch))
        
        if not answer:
            answer.append(int(expression[0]))
        return answer

    
    def operation(self, x, y, op):
        if op == '+': return x + y
        if op == '-': return x-y
        if op == '*': return x*y

if input.isdigit():
            m[input] = int(input)
            return [int(input)]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[input] = ret
        return ret        
"""