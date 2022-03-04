'''
    https://leetcode.com/problems/bulls-and-cows/

    299. Bulls and Cows

    You are playing the Bulls and Cows game with your friend.

    You write down a secret number and ask your friend to guess what the number is.
    When your friend makes a guess, you provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position.
    Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
    Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret
    and guess may contain duplicate digits.
'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls_count = 0
        cows_count = 0

        secret_digits_to_match = {}

        # we first map each digit in secret to its count in secret
        for digit in secret:
            if digit in secret_digits_to_match:
                secret_digits_to_match[digit] += 1
            else:
                secret_digits_to_match[digit] = 1

        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                # matched secret[i] to guess[i] so we need
                # reduce the count of digits in secret to match
                secret_digits_to_match[secret[i]] -= 1
                bulls_count += 1

        # now that we matched all the digits in secrets to the matching ones (in terms of value and position)
        # in guess, we need to check if there are characters in guess that are in secret but same index as anything
        # in bulls_indices
        for j in range(0, len(guess)):
            if secret[j] != guess[j] and guess[j] in secret_digits_to_match and secret_digits_to_match[guess[j]] > 0:
                secret_digits_to_match[guess[j]] -= 1
                cows_count += 1

        return str(bulls_count) + "A" + str(cows_count) + "B"


# secret = "1807"
# guess = "7810"

# secret = "1123"
# guess = "0111"

secret = "11"
guess = "10"
print(Solution().getHint(secret, guess))
