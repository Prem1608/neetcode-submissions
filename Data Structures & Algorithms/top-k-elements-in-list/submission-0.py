class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1=dict()
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        vals = sorted(dict1.items(), key=lambda items:items[1])
        res = dict(vals)
        ans = list(res.keys())
        return ans[(len(ans)-k):]