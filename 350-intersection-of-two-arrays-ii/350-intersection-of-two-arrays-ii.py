from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1.intersection(set2)
        count1 = dict(Counter(nums1))
        count2 = dict(Counter(nums2))
        output = []
        
        for num in intersection:
            count = min(count1[num], count2[num])
            output.extend([num] * count)
        
        return output
        
        