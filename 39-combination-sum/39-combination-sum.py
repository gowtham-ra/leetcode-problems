class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(rem, comb, start):
            if rem == 0:
                output.append(list(comb))
            elif rem < 0:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(rem-candidates[i], comb, i)
                comb.pop()
        
        backtrack(target, [], 0)
        
        return output
            
        