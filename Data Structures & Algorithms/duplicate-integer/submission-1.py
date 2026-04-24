class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fq={}
        for num in nums:
            if num in fq:
                fq[num]+=1
            else:
                fq[num]=1
        for key,value in fq.items():
            if value >= 2:
                return True
        return False
