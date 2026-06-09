class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        l = len(nums)
        while(i<l-1):
            j=i+1
            while(j<l):
                if target== nums[i]+nums[j]:
                    return [i,j]
                else:
                    j+=1
            i+=1
        
            