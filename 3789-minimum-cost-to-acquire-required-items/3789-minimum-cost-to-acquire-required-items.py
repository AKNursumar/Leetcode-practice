class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        a = costBoth*max(need1,need2)
        b = cost1*need1 + cost2*need2
        if need1>need2:
            c = costBoth*need2 + (need1-need2)*cost1
        else:
            c = costBoth*need1 + (need2-need1)*cost2
        return min(a,b,c)