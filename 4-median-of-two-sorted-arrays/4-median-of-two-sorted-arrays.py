class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = len(nums1)
        R = len(nums2)
        l = 0
        r = 0
        sorted_arr = []
        
        while l < L and r < R:
            if nums1[l] < nums2[r]:
                sorted_arr.append(nums1[l])
                l += 1
            else:
                sorted_arr.append(nums2[r])
                r += 1
        
        while l < L:
                sorted_arr.append(nums1[l])
                l += 1       
        while r < R:
                sorted_arr.append(nums2[r])
                r += 1
        
        mid = (L + R) // 2
        
        if len(sorted_arr) % 2 == 0:
            return (sorted_arr[mid-1] + sorted_arr[mid]) / 2
        else:
            return sorted_arr[mid]
        