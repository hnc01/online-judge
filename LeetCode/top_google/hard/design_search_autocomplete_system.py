'''
    https://leetcode.com/problems/design-search-autocomplete-system/

    642. Design Search Autocomplete System

    Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and
    end with a special character '#').

    You are given a string array sentences and an integer array times both of length n where sentences[i] is a
    previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each
    input character except '#', return the top 3 historical hot sentences that have the same prefix as the part
    of the sentence already typed.

    Here are the specific rules:
        - The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
        - The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
          If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
        - If less than 3 hot sentences exist, return as many as you can.
        - When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

    Implement the AutocompleteSystem class:
        - AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
        - List<String> input(char c) This indicates that the user typed the character c.
        - Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
        - Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.
          If there are fewer than 3 matches, return them all.
'''

'''
    Accepted. Done using prefix trees.
'''


class AutocompleteSystem:
    class Node:
        value = None
        next = None
        sentences = None

        def __init__(self, value):
            self.value = value
            self.next = []
            self.sentences = set()

    roots = None
    sentenceHotDegree = None
    inputSentence = None
    inspectionRoot = None

    def __init__(self, sentences: [str], times: [int]):
        self.roots = []
        self.sentenceHotDegree = {}
        self.inputSentence = ''
        self.inspectionRoot = None

        # create prefix trees out of all the entries in sentences
        for s in range(0, len(sentences)):
            sentence = sentences[s]

            # mapping each sentence to its number of occurrences
            self.sentenceHotDegree[sentence] = times[s]

            # first let's see if the first character in sentence is a root we've already seen
            currentRoot = None

            for root in self.roots:
                if root.value == sentence[0]:
                    currentRoot = root

                    break

            if currentRoot is None:
                # we couldn't find an existing root for sentence so we create a new one
                newRoot = self.Node(sentence[0])

                self.roots.append(newRoot)

                currentRoot = newRoot

            currentRoot.sentences.add(sentence)

            for i in range(1, len(sentence)):
                currentChar = sentence[i]

                childNode = None

                # check if any of the children of currentRoot are currentChar
                for child in currentRoot.next:
                    if child.value == currentChar:
                        childNode = child

                        break

                if childNode is None:
                    # we couldn't find a path for the sentence so we keep paving the way
                    newChild = self.Node(currentChar)

                    currentRoot.next.append(newChild)

                    childNode = newChild

                childNode.sentences.add(sentence)

                currentRoot = childNode

            # when we reach here, currentRoot is a leaf node denoting the last letter of a sentence
            # we need to add to it the child # to mark the end of a sentence (this will cover our case
            # when there are sentences that are prefixes are other sentences) => we don't want them to get lost
            endOfSentenceChild = self.Node('#')

            currentRoot.next.append(endOfSentenceChild)

    def input(self, c: str) -> [str]:
        # first let's see if this the beginning of a new sentence of we're in the middle of one
        if self.inputSentence == '':
            # we're starting new so we need to find our root
            if c != '#':
                self.inputSentence += c

            for root in self.roots:
                if root.value == c:
                    self.inspectionRoot = root
                    break

            # we're done trying to find the root
            if self.inspectionRoot is None:
                # we couldn't find a root for our sentence => it needs its own root
                newRoot = self.Node(c)

                self.roots.append(newRoot)

                self.inspectionRoot = newRoot

            # whether we found an existing root or we created a new one, we return the hot sentences
            return self.getHotSentences()
        else:
            if c != '#':
                self.inputSentence += c

            # we're in the middle of processing this sentence
            # we grab the new character and try to see if we can find matches for it in our current root
            for child in self.inspectionRoot.next:
                if child.value == c:
                    self.inspectionRoot = child

                    hotSentences = self.getHotSentences()

                    if c == '#':
                        # we need to reset our search
                        self.resetSearch()

                    return hotSentences

            # if we reached here it means that sentence we're one doesn't have a path => add path
            newChild = self.Node(c)

            self.inspectionRoot.next.append(newChild)

            self.inspectionRoot = newChild

            hotSentences = self.getHotSentences()

            if c == '#':
                # we need to reset our search
                # getHotSentences() would still work because # nodes don't have any sentences attached to them
                # so we would always return [] in their case
                self.resetSearch()

            return hotSentences

    def getHotSentences(self):
        # get all the sentences under this root
        allSentences = list(self.inspectionRoot.sentences)

        # sort the sentences by hot degree and then by alphabet
        allSentences.sort(key=lambda x: (-self.sentenceHotDegree[x], x))

        return allSentences[0:3]

    def resetSearch(self):
        # we just finished an input sentence
        # we have 2 cases:
        # either this is a sentence we've seen before (we didn't add a new path to tree)
        # OR this was a new sentence
        if self.inputSentence in self.sentenceHotDegree:
            # this is a sentence we've seen before (we didn't add a new path to tree)
            self.sentenceHotDegree[self.inputSentence] += 1
        else:
            # this was a new sentence
            self.sentenceHotDegree[self.inputSentence] = 1

            # add this sentence to node.sentences along the new path
            currentRoot = None

            for root in self.roots:
                if root.value == self.inputSentence[0]:
                    currentRoot = root
                    currentRoot.sentences.add(self.inputSentence)

                    break

            # no need to check if currentRoot is None because we know we already
            # added the path for this sentence
            # since we don't add # to our inputSentence, we know that the sentence won't
            # be added to #'s list of sentences
            for i in range(1, len(self.inputSentence)):
                for child in currentRoot.next:
                    if child.value == self.inputSentence[i]:
                        child.sentences.add(self.inputSentence)
                        currentRoot = child

                        break

        self.inputSentence = ''
        self.inspectionRoot = None


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
#
# # params = [["i"], [" "], ["l"], ["o"], ["v"], ["e"], [" "], ["y"], ["o"], ["u"], ["#"]]
# params = [["i"], [" "], ["l"], ["o"], ["v"], ["e"], ["#"], ["i"], ["#"]]
#
# for param in params:
#     print(obj.input(param[0]))

# ["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input","input","input"]
# [[["abc","abbc","a"],[3,3,3]],["b"],["c"],["#"],["b"],["c"],["#"],["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]]

obj = AutocompleteSystem(["abc", "abbc", "a"], [3, 3, 3])

params = [["b"], ["c"], ["#"], ["b"], ["c"], ["#"], ["a"], ["b"], ["c"], ["#"], ["a"], ["b"], ["c"], ["#"]]

for param in params:
    print(obj.input(param[0]))
