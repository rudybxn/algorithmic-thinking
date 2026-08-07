class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # lowest rate can be 1
        # highest can be max of pile
        # check each rate and store if smaller or equal to h. we need to find smallest possible workable rate

        lo = 1
        hi = max(piles)
        optimal = hi
        while lo<=hi:
            rate = lo+(hi-lo)//2
            timetaken = 0
            for num in piles:
                timetaken+=math.ceil(num/rate)
            if timetaken<=h:
                optimal = rate
                hi = rate - 1
            else:
                lo = rate + 1

        return optimal
            