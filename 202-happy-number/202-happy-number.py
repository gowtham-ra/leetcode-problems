class Solution:
    def isHappy(self, n: int) -> bool:
        repeated = {n}
        while n != 1:
            ch = str(n)            
            summ = 0
            
            for dig in ch:
                summ += int(dig) ** 2
            
            if summ in repeated:
                return False
            
            n = summ
            repeated.add(n)
        
        return True
            
                
                
        