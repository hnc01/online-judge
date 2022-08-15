class Solution:
    def myAtoi(self, s: str) -> int:
        lowerBound = - 2 ** 31
        upperBound = (2 ** 31) - 1

        digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
        }

        # step 1
        s = s.lstrip()

        # step 2
        if len(s) > 0:
            sign = '+'
            result = ""
            i = 0

            # check the sign of the integer
            if s[i] == '-':
                sign = '-'
                i += 1
            elif s[i] == '+':
                i += 1


            while i < len(s) and s[i] in digits:
                result += s[i]
                i += 1

            # we reach here when we encounter the first non-digit character or end of input
            resultInt = 0
            place = 1

            for j in range(len(result) - 1, -1, -1):
                resultInt += (digits[result[j]]) * place
                place *= 10

            if sign == '-':
                resultInt = -1 * resultInt

            if resultInt < lowerBound:
                return lowerBound
            elif resultInt > upperBound:
                return upperBound
            else:
                return resultInt
        else:
            return 0