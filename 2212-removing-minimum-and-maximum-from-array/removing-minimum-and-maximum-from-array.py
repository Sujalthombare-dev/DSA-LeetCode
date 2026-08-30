class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # Get the individual positions
        idx_max = nums.index(max(nums))
        idx_min = nums.index(min(nums))
        
        # Order them cleanly as leftmost and rightmost markers
        low = min(idx_max, idx_min)
        high = max(idx_max, idx_min)
        n = len(nums)
        
        # Compare all three valid elimination vectors
        del_left = high + 1
        del_right = n - low
        del_both = (low + 1) + (n - high)
        
        return min(del_left, del_right, del_both)
