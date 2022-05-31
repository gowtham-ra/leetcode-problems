class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mapp = {}
        maxi = float('-inf')
        
        while (lowLimit <= highLimit):
            val = sum(map(int, list(str(lowLimit))))
            if val not in mapp:
                mapp[val] = 1
            else:
                mapp[val] += 1
            
            maxi = max(mapp[val], maxi)
            lowLimit += 1
        
        return maxi
            