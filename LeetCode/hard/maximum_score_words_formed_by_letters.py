'''
    https://leetcode.com/problems/maximum-score-words-formed-by-letters/

    1255. Maximum Score Words Formed by Letters


    Given a list of words, list of  single letters (might be repeating) and score of every character.

    Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

    It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z'
    is given by score[0], score[1], ... , score[25] respectively.
'''

'''
    Accepted
'''

class Solution:
    def maxScoreWords(self, words: [str], letters: [str], score: [int]) -> int:
        # returns true if a word can be formed by given letters
        def isValidSet(wordSet, letterCount):
            for letter in wordSet:
                if letter not in letterCount or letterCount[letter] < wordSet[letter]:
                    return False

            return True

        def calculateSetScore(wordSet, letterScore):
            setScore = 0

            for letter in wordSet:
                setScore += wordSet[letter] * letterScore[letter]

            return setScore

        '''
            Start: Preprocessing
        '''
        # first, we map each character to its score
        letterScore = {}

        for i in range(0, len(score)):
            letterScore[chr(ord('a') + i)] = score[i]

        # second, we map the letters to their count to quickly check if a letter is present and its freq
        letterCount = {}

        for letter in letters:
            if letter not in letterCount:
                letterCount[letter] = 0

            letterCount[letter] += 1

        # third, we transform every word into a map of letter counts
        # we ignore in the process all the words that can't be formed by our given letters
        bagOfWords = []

        for word in words:
            wordLetterCount = {}

            isValidWord = True

            for letter in word:
                if letter not in letterCount:
                    isValidWord = False
                    break

                if letter not in wordLetterCount:
                    wordLetterCount[letter] = 0

                wordLetterCount[letter] += 1

            if isValidWord:
                bagOfWords.append(wordLetterCount)

        '''
            End: Preprocessing
        '''

        '''
            Start: Solution
        '''
        emptyWordSet = {}

        for letter in letterCount:
            emptyWordSet[letter] = 0

        # each wordSet is a tuple of letters in the set and the indices of words used
        wordSets = [(emptyWordSet, [])]

        # to keep track of sets we've seen before
        seenSets = []

        maxScore = 0

        while len(wordSets) > 0:
            # print(wordSets)
            newWordSets = []

            for wordSet in wordSets:
                for i in range(0, len(bagOfWords)):
                    # we haven't used this word in this set yet
                    if i not in wordSet[1]:
                        # try appending the current word to the set and see if we have a valid set
                        for letter in bagOfWords[i]:
                            wordSet[0][letter] += bagOfWords[i][letter]

                        if wordSet[0] not in seenSets:
                            seenSets.append(wordSet[0].copy())

                            if isValidSet(wordSet[0], letterCount):
                                # add this set to our new list of sets
                                indices = wordSet[1].copy()
                                indices.append(i)

                                newWordSets.append((wordSet[0].copy(), indices))

                                wordSetScore = calculateSetScore(wordSet[0], letterScore)

                                maxScore = max(maxScore, wordSetScore)

                        # reset this wordSet so we can try adding another word to it
                        for letter in bagOfWords[i]:
                            wordSet[0][letter] -= bagOfWords[i][letter]

            wordSets = newWordSets

        '''
            End: Solution
        '''

        return maxScore


# words = ["add", "dda", "bb", "ba", "add"]
# letters = ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c", "c", "d", "d", "d"]
# score = [3, 9, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

words = ["daeagfh","acchggghfg","feggd","fhdch","dbgadcchfg","b","db","fgchfe","baaedddc"]
letters =["a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d","d","d","e","e","e","e","e","e","e","e","e","e","f","f","f","f","f","f","f","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h","h","h","h","h","h","h"]
score = [2,1,9,2,10,5,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(Solution().maxScoreWords(words, letters, score))
