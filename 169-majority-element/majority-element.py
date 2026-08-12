class Solution(object):
    def majorityElement(self, nums):
        count, result = 0, 0
        for i in nums:
            if count == 0:
                result = i
            if i == result:
                count += 1
            else:
                count -= 1
            
            i += 1
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        