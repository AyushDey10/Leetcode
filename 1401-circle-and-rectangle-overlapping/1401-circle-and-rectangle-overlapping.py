class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        dx = xCenter - closestX
        dy = yCenter - closestY

        return dx * dx + dy * dy <= radius * radius        