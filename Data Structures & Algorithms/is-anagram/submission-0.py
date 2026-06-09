class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1=dict()
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1
        for i in range((len(t))):
            if t[i] not in dict1:
                return False
            else:
                dict1[t[i]]-=1
        return all(value==0 for value in dict1.values())