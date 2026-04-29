class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # create
        # 3:[1,4,2]
        # check len(3)=n-1
        inc = defaultdict(int)
        out = defaultdict(int)

        for src,dst in trust:
            out[src]+=1
            inc[dst]+=1
        
        for i in range(1,n+1):
            if out[i] == 0 and inc[i] == n-1:
                return i

        return -1
        
