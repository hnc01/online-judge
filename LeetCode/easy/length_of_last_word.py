class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        sArray = s.split(' ')

        return len(sArray[-1])