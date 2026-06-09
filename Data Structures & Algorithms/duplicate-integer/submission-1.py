class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = dict()
        for n in nums:
            if n not in dict1:
                dict1[n]=1
            else:
                return True
        return False