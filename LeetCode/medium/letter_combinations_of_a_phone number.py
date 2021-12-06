'''
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

'''
    Accepted
'''

class Solution:
    def create_digits_letters_map(self):
        digits_letters_map = {}

        digits_letters_map[2] = ['a', 'b', 'c']
        digits_letters_map[3] = ['d', 'e', 'f']
        digits_letters_map[4] = ['g', 'h', 'i']
        digits_letters_map[5] = ['j', 'k', 'l']
        digits_letters_map[6] = ['m', 'n', 'o']
        digits_letters_map[7] = ['p', 'q', 'r', 's']
        digits_letters_map[8] = ['t', 'u', 'v']
        digits_letters_map[9] = ['w', 'x', 'y', 'z']

        return digits_letters_map

    def letterCombinations(self, digits: str) -> []:
        if len(digits) <= 0:
            return []
        else:
            digits_letters_map = self.create_digits_letters_map()

            solutions = []

            for character in digits:
                digit = int(character)

                if digit in digits_letters_map:
                    possible_letters = digits_letters_map[digit]

                    temp_solutions = []

                    if len(solutions) > 0:
                        for solution in solutions:
                            for possible_letter in possible_letters:
                                temp_solutions.append(solution + possible_letter)
                    else:
                        for possible_letter in possible_letters:
                            temp_solutions.append(possible_letter)

                    solutions = temp_solutions

            return solutions


print(Solution().letterCombinations("2"))
