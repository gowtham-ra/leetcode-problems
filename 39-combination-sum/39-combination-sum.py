class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n = len(candidates)
        self.ans = []
        self.candidates = candidates
        self.combSum(0, target, [])
        
        
        return self.ans
            
    def combSum(self, idx, target, lis):
        if idx == self.n:
            if target == 0:
                self.ans.append(lis.copy())
            return
        
        if target - self.candidates[idx] >= 0:
            lis.append(self.candidates[idx])
            target -= self.candidates[idx]
            self.combSum(idx, target, lis)
            lis.pop()
            target += self.candidates[idx]
        
        self.combSum(idx+1, target, lis)
            
        