class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]

        strmap = defaultdict(list)
        for s in strs:
            s_srt = "".join(sorted(s))
            if s_srt in strmap:
                strmap[s_srt].append(s)
            else:
                strmap[s_srt] = [s]
        
        ret_list = []
        for k,v in strmap.items():
            l = []
            for val in v:
                l.append(val)
            ret_list.append(l)

        return ret_list