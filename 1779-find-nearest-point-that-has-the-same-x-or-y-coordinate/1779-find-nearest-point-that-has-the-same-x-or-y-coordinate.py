class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m = float("inf")
        ind = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1]==y:
                if m>min(m,abs(points[i][0]-x)+abs(points[i][1]-y)):
                    ind = i
                    m = min(m,abs(points[i][0]-x)+abs(points[i][1]-y))
        return ind
        