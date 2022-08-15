class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        # getting the length of the words
        n = len(words[0])

        def isValidSubstring(currentSubstring, wordCount):
            currentSubstringCount = {}

            for word in wordCount:
                currentSubstringCount[word] = 0

            for i in range(0, len(currentSubstring), n):
                currentWord = currentSubstring[i:i + n]

                if currentWord in currentSubstringCount:
                    currentSubstringCount[currentWord] += 1
                else:
                    # the current word doesn't exist in our list of words
                    return False

            # now that we're sure all the words in currentSubstring are valid, we check their count
            for word in wordCount:
                if wordCount[word] != currentSubstringCount[word]:
                    return False

            return True

        targetSubstringLength = n * len(words)

        wordCount = {}

        for word in words:
            if word not in wordCount:
                wordCount[word] = 0

            wordCount[word] += 1

        result = []

        for i in range(0, len(s)):
            # check if substring at i gives a correct result
            if i + targetSubstringLength <= len(s):
                currentSubstring = s[i:i + targetSubstringLength]

                if isValidSubstring(currentSubstring, wordCount):
                    result.append(i)
            else:
                # the remaining string is too small to be generated from `words`
                break

        return result