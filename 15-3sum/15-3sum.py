class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        N = len(nums)
        
        if N < 3:
            return triplets
        
        nums.sort()
        for i in range(N-2):
            j = i+1
            k = N-1
            
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    
                    if triplet not in triplets:
                        triplets.append(triplet)
                    
                    j += 1
                elif summ < 0:
                    j += 1
                else:
                    k -= 1   
                    
        return triplets
    