class Solution(object):
    def sortArray(self, nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        result = []
        i = 0
        j = 0

        # Merge two sorted arrays
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Remaining elements from left
        while i < len(left):
            result.append(left[i])
            i += 1

        # Remaining elements from right
        while j < len(right):
            result.append(right[j])
            j += 1

        return result