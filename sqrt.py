class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            result = x / 2
        
            while result * result > x + 0.1:
                result = (result + x / result) / 2
        
        return int(result)
