'''
    https://leetcode.com/problems/implement-trie-prefix-tree/

    208. Implement Trie (Prefix Tree)

    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
    There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

        - Trie() Initializes the trie object.
        - void insert(String word) Inserts the string word into the trie.
        - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

# TODO note that it's best if the end of a string is marked by a tree node `$` for example so that words like `apple` and `app` can fit distincly into tree
# check notebook