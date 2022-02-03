class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [sum(banks) for banks in accounts]
        
        return max(wealth)
        
        