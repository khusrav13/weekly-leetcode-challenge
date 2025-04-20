class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        """
        Helper function to reverse a portion of the array in-place.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1