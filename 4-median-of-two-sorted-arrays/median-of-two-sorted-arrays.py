class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num3=nums1+nums2
        num3.sort()
        if len(num3)%2!=0:
            return float(num3[len(num3)/2])
        else:
            n1=float(num3[len(num3)/2])
            n2=float(num3[(len(num3)/2)-1])
            return (n1+n2)/2

        