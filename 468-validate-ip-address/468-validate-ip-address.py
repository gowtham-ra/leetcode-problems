class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIPv4(IP):
            nums = IP.split('.')
            
            for num in nums:
                if not num or (num[0] == '0' and len(num) != 1):
                    return "Neither"
                
                if not all(ch.isdigit() for ch in num):
                    return "Neither"
                
                num = int(num)
                
                if num > 255 or num < 0:
                    return "Neither"
            
            return "IPv4"
        
        def checkIPv6(IP):
            nums = IP.split(':')
            hexa = "0123456789abcdefABCDEF"
            
            for num in nums:
                if len(num) < 1 or len(num) > 4:
                    return "Neither"
                
                if not all(ch in hexa for ch in num):
                    return "Neither"
            
            return "IPv6"
        
        
        if queryIP.count('.') == 3:
            return checkIPv4(queryIP)
        elif queryIP.count(':') == 7:
            return checkIPv6(queryIP)
        else:
            return "Neither"

            
        
        
            
            

            
        
        
        
        