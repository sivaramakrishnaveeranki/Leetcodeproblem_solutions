# 4. Median of Two Sorted Arrays

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


 class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        num3=nums1+nums2
        num3.sort()
        n=len(num3)
        if n % 2==0:
            return (num3[n//2]+num3[n//2-1])/2.0

        else:
            return float(num3[n//2])

