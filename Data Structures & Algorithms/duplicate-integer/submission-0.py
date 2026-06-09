class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        res=False
        for i in range(0,l):
            if(nums.count(nums[i])>=2):
                res=True
                break
            else:
                res=False
        return res