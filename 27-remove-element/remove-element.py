class Solution(object):
    def removeElement(self, nums, val):
        res = []
        count = 0
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
        return count
       
        

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        