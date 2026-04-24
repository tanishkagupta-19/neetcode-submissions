class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmp={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in fmp:
                fmp[nums[i]]+=1
            else:
                fmp[nums[i]]=1
        sorted_items = sorted(fmp.items(), key=lambda x: x[1], reverse=True)
        for i in range(0, k):
            key, val = sorted_items[i]
            res.append(key)
        return res