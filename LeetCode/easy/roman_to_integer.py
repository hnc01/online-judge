class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToValue = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        result = 0
        i = 0

        while i < len(s):
            currentCharacter = s[i]

            if i + 1 < len(s):
                nextCharacter = s[i + 1]

                subString = currentCharacter + nextCharacter

                specialCases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

                if(subString in specialCases):
                    result += symbolToValue[nextCharacter] - symbolToValue[currentCharacter]  # result += 10 - 1 = 9
                    i += 2
                else:
                    result += symbolToValue[currentCharacter]
                    i += 1
            else:
                # process currentCharacter alone
                result += symbolToValue[currentCharacter]
                i += 1

        return result