'''
    https://leetcode.com/problems/guess-the-word/

    843. Guess the Word

    This is an interactive problem.

    You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

    You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with
    6 lowercase letters.

    This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.
    Also, if your guess is not in the given wordlist, it will return -1 instead.

    For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer
    calls to Master.guess and at least one of these guesses was secret, then you pass the test case.

    Constraints:
    - 1 <= wordlist.length <= 100
    - wordlist[i].length == 6
    - wordlist[i] consist of lowercase English letters.
    - All the strings of wordlist are unique.
    - secret exists in wordlist.
    - numguesses == 10
'''

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
import random


class Master:
    def __init__(self, secret: str, wordList: [str]):
        self.secret = secret
        self.wordList = wordList

    def guess(self, word: str) -> int:
        if word not in self.wordList:
            return -1

        commonLetters = 0

        for i in range(0, len(self.secret)):
            if word[i] == self.secret[i]:
                commonLetters += 1

        return commonLetters


'''
    Accepted
'''


class Solution:
    def findSecretWord(self, wordlist: [str], master: Master) -> None:
        # first we'll compute the intersection of every word with every other word
        # this will map every word to every other word and hold the intersection between the words
        wordsIntersections = {}

        # list of words that are still an option
        validWords = []

        for i in range(0, len(wordlist)):
            currentWord = wordlist[i]

            wordsIntersections[currentWord] = []
            # at the beginning, all words are valid options
            validWords.append(currentWord)

            for j in range(0, len(wordlist)):
                if i != j:
                    otherWord = wordlist[j]

                    commonLetters = 0

                    for h in range(0, len(currentWord)):
                        if currentWord[h] == otherWord[h]:
                            commonLetters += 1

                    wordsIntersections[currentWord].append((otherWord, commonLetters))

        # guessesCount = 0

        # now we can start guessing, we'll go through the list of valid words and keep guessing until we get the right answer
        while True:
            # first we make sure that we still have valid word options
            # this case should never happen because we should have guessed the word by now
            if len(validWords) <= 0:
                break

            # choose a random valid word
            currentWord = validWords[random.randint(0, len(validWords) - 1)]

            # after choosing the word, we ask master to guess to see if it's the right answer
            commonLetters = master.guess(currentWord)

            # guessesCount += 1

            # print('master.guess("' + currentWord + '") returns ' + str(commonLetters) + ', because "' + currentWord + '" has ' + str(commonLetters) + ' matches.')

            if commonLetters == 6:
                # if the word we guessed has all letters in common with the secret and in same position
                # then the guesses word is the correct word and we can exit the program
                break
            else:
                # get all the words that have `commonLetters` intersection with `currentWord`
                # all the other words are now invalid
                newValidWords = []

                for otherWord, intersection in wordsIntersections[currentWord]:
                    if otherWord in validWords and intersection == commonLetters:
                        newValidWords.append(otherWord)

                validWords = newValidWords

                # print("now the valid words are [" + str(len(validWords)) + "] " + str(validWords))

        # print(guessesCount)


# wordlist = ["abcczz", "acckzz","ccbazz","eiowzz"]
#
# master = Master('acckzz', wordlist)
#
# Solution().findSecretWord(wordlist, master)

# wordlist = ["hamada","khaled"]
#
# master = Master('hamada', wordlist)
#
# Solution().findSecretWord(wordlist, master)

# wordlist = ['sultry', 'numero', 'arezzo', 'dermot', 'crosby', 'hodder', 'kahuna', 'vitara', 'kaiser', 'reebok', 'exilim', 'kenyan', 'acxiom', "textrm", "bidder", "choker", "tawnee", "payoff",
#             "marist", "avenge", "kenyon", "sheila", "arnaud", "nextel", "purify", "profil", "toucan", "samoan", "mamiya", "manage", "takeda", "uncles", "mayhew", "microm", "carpal", "rhymes",
#             "honour", "kansai", "wiping", "winsor", "tiffin", "astron", "bettie", "dozens", "kohler", "realms", "misfit", "models", "routed", "pacing", "bodega", "cursed", "onward", "brahma",
#             "userid", "modems", "source", "hitter", "pietro", "richie", "cowell", "marvin", "corrie", "loomis", "rafael", "boosts", "alerts", "vhosts", "taylor", "regime", "creole", "extent",
#             "holmes", "baroda", "cinema", "genres", "illini", "selena", "rifles", "sonora", "hendon", "tenchi", "risers", "womack", "fathom", "slavic", "wicker", "citrus", "neogeo", "sorbet",
#             "maximo", "squirt", "awards", "gaston", "gallop", "porter", "bumble", "vorbis", "indoor", "siebel"]
#
# master = Master('gallop', wordlist)
#
# Solution().findSecretWord(wordlist, master)

# wordlist = ["cognac", "brakes", "maxxum", "brahms", "undies", "fellas", "dupont", "darrow", "giggle", "roscoe", "malawi", "whoops", "coyote", "aitken", "morale", "plated", "iodine", "bourse",
#             "infect", "poorly", "remand", "gagnon", "action", "rodent", "spylog", "kamera", "shards", "diwali", "orient", "camels", "menace", "pieter", "eskimo", "parted", "celery", "permis",
#             "beamed", "shears", "report", "winona", "mystic", "kisses", "newsre", "brazen", "within", "royals", "belief", "alonzo", "manson", "sawyer", "romani", "reagan", "onefit", "invest",
#             "jurors", "bidpay", "conway", "livers", "galaxy", "crimea", "bolton", "pelosi", "hodges", "havent", "aligns", "caused", "invert", "jungle", "office", "mammal", "protec", "window",
#             "sorter", "fanart", "bakery", "ectaco", "enduro", "tailor", "barely", "agence", "buxton", "tenure", "spring", "astral", "sonora", "hanson", "nikita", "eulogy", "howard", "covers",
#             "sadler", "membre", "howell", "cooley", "daniel", "nasdaq", "paulus", "oliver", "slalom", "polled"]
#
#
# master = Master('galaxy', wordlist)
#
# Solution().findSecretWord(wordlist, master)

wordlist = ["wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc", "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh",
            "phuepp", "rokoro", "nxcwmo", "awvqlr", "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad", "uslult", "rtjosi", "hsygda",
            "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn", "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud",
            "jjinfa", "kqbttl", "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty", "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda",
            "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg", "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh", "reeyhj", "vmcwaf",
            "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv", "srxuus", "pydgmq"]

master = Master('ccoyyo', wordlist)

Solution().findSecretWord(wordlist, master)
