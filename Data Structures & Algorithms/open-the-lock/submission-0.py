class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # start at 0000

        visit = set()
        for d in deadends:
            if d == "0000": # dead list check
                return -1
            visit.add(d) # track deadends as visited nodes

        q = deque()
        q.append(("0000",0))
        visit.add("0000")

        def neighbors(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit = str((int(lock[i]) - 1+10)%10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res

        
        while q:
            cand, turns = q.popleft()
            if cand == target:
                return turns
            for c in neighbors(cand):
                if c not in visit:
                    visit.add(c)
                    q.append((c,turns+1))

        return -1