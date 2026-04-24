class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps={}
        for s in strs:
            st="".join(sorted(s))
            if st not in maps:
                maps[st]=[]
            maps[st].append(s)
        return list(maps.values())
