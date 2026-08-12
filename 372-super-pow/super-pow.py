class Solution(object):
    def superPow(self, a, b):
        k = 0

        for i in b:
            k = k*10 + i

            # if k > 1337:
            #     break
        return pow(a,k,1337)
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        