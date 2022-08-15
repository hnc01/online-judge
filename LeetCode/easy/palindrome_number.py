class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        xReverse = 0
        xCopy = x

        while xCopy > 0:
            xReverse = (xReverse * 10) + (xCopy % 10)
            xCopy //= 10

        return x == xReverse