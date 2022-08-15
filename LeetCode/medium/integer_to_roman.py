class Solution:
    def intToRoman(self, num: int) -> str:
        numeralsMap = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        sortedNumerals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        result = ""

        while num > 0:
            # find the first numeral <= num
            for i in range(len(sortedNumerals) - 1, -1, -1):
                if sortedNumerals[i] <= num:
                    # we found our first numeral
                    result += numeralsMap[sortedNumerals[i]]
                    num -= sortedNumerals[i]
                    break

        return result
