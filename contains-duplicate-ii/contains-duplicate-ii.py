class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        
        for idx, num in enumerate(nums):
            if num in mapp:
                diff = abs(mapp[num] - idx)                
                if diff <= k:
                    return True
            
            mapp[num] = idx
        
        return False
        