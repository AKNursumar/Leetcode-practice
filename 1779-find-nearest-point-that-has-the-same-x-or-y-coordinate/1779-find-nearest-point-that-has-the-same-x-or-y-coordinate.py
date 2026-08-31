class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m = float("inf")
        ind = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1]==y:
                dist = abs(points[i][0]-x)+abs(points[i][1]-y)
                if m> dist:
                    ind = i
                    m = dist
        return ind
        