class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slope with respect to first point is always the same

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False

        return True
