class Solution:
    def uniformArray(self, nums1):
        if all(x % 2 == 0 for x in nums1):
            return True
        
        return min(nums1) % 2 == 1