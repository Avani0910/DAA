class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max = nums[0]

        start = 0
        ans_start = 0
        ans_end = 0


        for i in range(len(nums)):
            if sum == 0:
                start = nums[i]

            sum += nums[i]
            if sum > max:
                max = sum
                ans_start = start
                ans_end = i
            if sum < 0:
                sum = 0
        return max
        """
        :type nums: List[int]
        :rtype: int
        """
        