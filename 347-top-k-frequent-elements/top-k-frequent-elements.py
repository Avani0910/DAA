class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_arr = sorted(freq, key=freq.get, reverse = True)

        return sorted_arr[:k]


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        