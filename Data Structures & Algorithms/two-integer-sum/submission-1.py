class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        i=0

        while(i<l):
            for j in range(i+1,l):
                if target==(nums[i]+nums[j]):
                    return [i,j]
            i+=1
                
            