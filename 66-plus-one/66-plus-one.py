class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = digits[-1]
        num += 1
        
        if num < 10:
            digits[-1] = num
            return digits
        else:
            digits[-1] = 0
            add = 1
            
            for i in range(len(digits)-2, -1, -1):
                num = digits[i]

                if not add:
                    continue
                else:
                    if num == 9:
                        digits[i] = 0
                        add = 1
                    else:
                        digits[i] += add
                        add = 0
                
            if add:
                digits.insert(0, 1)

            return digits

            
        
        
        
        