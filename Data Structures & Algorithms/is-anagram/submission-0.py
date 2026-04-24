class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fq1={}
        fq2={}
        for st in s:
            if st in s:
                if st not in fq1:
                    fq1[st]=1
                else:
                    fq1[st]+=1
        for st in t:
            if st in t:
                if st not in fq2:
                    fq2[st]=1
                else:
                    fq2[st]+=1
        if fq1==fq2:
            return True
        return False
        