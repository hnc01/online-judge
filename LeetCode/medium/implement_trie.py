'''
    https://leetcode.com/problems/implement-trie-prefix-tree/

    208. Implement Trie (Prefix Tree)

    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
    There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

        - Trie() Initializes the trie object.
        - void insert(String word) Inserts the string word into the trie.
        - boolean search(String word) Returns True if the string word is in the trie (i.e., was inserted before), and False otherwise.
        - boolean startsWith(String prefix) Returns True if there is a previously inserted string word that has the prefix prefix, and False otherwise.
'''


class Trie:
    trees_nodes = None  # maps character -> array of nodes
    trees_children = None  # maps character -> map from index to set
    trees_roots = None  # list of roots of trees

    def __init__(self):
        self.trees_nodes = {}
        self.trees_children = {}
        self.trees_roots = []

    def insert(self, word: str) -> None:
        if word:
            # the character doesn't belong to any tree
            if word[0] not in self.trees_roots:
                prev = None  # index of parent node
                current_tree_nodes = None
                current_tree_children = None

                for character in word:
                    if prev is None:
                        # the character is the root of the tree
                        self.trees_roots.append(character)
                        current_tree_root = character

                        self.trees_nodes[current_tree_root] = []
                        self.trees_children[current_tree_root] = {}

                        current_tree_nodes = self.trees_nodes[current_tree_root]
                        current_tree_children = self.trees_children[current_tree_root]

                        current_tree_nodes.append(character)

                        current_character_index = len(current_tree_nodes) - 1

                        # this is the first node we ever add
                        prev = current_character_index
                    else:
                        # adding the new node to the tree rooted at current_tree_root
                        current_tree_nodes.append(character)

                        current_character_index = len(current_tree_nodes) - 1

                        # we add the current character as a child of prev
                        if prev in current_tree_children:
                            current_tree_children[prev].add(current_character_index)
                        else:
                            temp = set()
                            temp.add(current_character_index)

                            current_tree_children[prev] = temp

                        prev = current_character_index

                # add the end of word character
                if prev in current_tree_children:
                    # adding a -1 index to mark the end of the string
                    current_tree_children[prev].add(-1)
                else:
                    temp = set()
                    temp.add(-1)

                    current_tree_children[prev] = temp
            else:
                # the character belongs to a tree

                # there are already nodes in the the tree so we need to trace the word until the end
                # first we check if the character at 0 matches the root of the tree (because in subsequent steps we need to check the next character always)
                current_root_character = word[0]

                current_tree_nodes = self.trees_nodes[current_root_character]
                current_tree_children = self.trees_children[current_root_character]

                node_index = 0  # we start at the root

                # we can proceed
                # we can proceed testing the first character because we already know the tree's root is the same character
                for character in word[1:]:
                    # check if any of the children of current node have the character
                    if node_index in current_tree_children:
                        node_children = current_tree_children[node_index]

                        found_match = False

                        for child_index in node_children:
                            if child_index != -1 and current_tree_nodes[child_index] == character:
                                # we can proceed with this child
                                node_index = child_index
                                found_match = True
                                break

                        if not found_match:
                            # none of the children of current node match the character so we need to add it
                            current_tree_nodes.append(character)
                            current_character_index = len(current_tree_nodes) - 1

                            current_tree_children[node_index].add(current_character_index)
                            node_index = current_character_index
                    else:
                        # we didn't find any children of the current node that have this character so we need to add it
                        current_tree_nodes.append(character)
                        current_character_index = len(current_tree_nodes) - 1

                        temp = set()
                        temp.add(current_character_index)
                        current_tree_children[node_index] = temp

                        node_index = current_character_index

                # finally when we are done adding the word, we add the end of character index
                if node_index in current_tree_children:
                    current_tree_children[node_index].add(-1)
                else:
                    temp = set()
                    temp.add(-1)
                    current_tree_children[node_index] = temp

    def search(self, word: str) -> bool:
        return self.search_helper(word, 'exact')

    def startsWith(self, prefix: str) -> bool:
        return self.search_helper(prefix, 'prefix')

    def search_helper(self, word, type):
        # first we need to know which tree to look through
        tree_root = word[0]

        if tree_root not in self.trees_roots:
            return False

        # here we know that there is a tree rooted at tree_root
        current_tree_nodes = self.trees_nodes[tree_root]
        current_tree_children = self.trees_children[tree_root]

        # type = 'exact' or type = 'prefix'
        if len(current_tree_nodes) > 0:
            # the tree is not empty so we can search
            node_index = 0

            for character in word[1:]:
                if node_index in current_tree_children:
                    current_node_children = current_tree_children[node_index]

                    character_found = False

                    for child_index in current_node_children:
                        if child_index != -1 and current_tree_nodes[child_index] == character:
                            # we found a child that matches current character
                            node_index = child_index
                            character_found = True
                            break

                    if not character_found:
                        return False
                else:
                    # we're not done with the string but there are no more characters in branch
                    return False

            if type == 'exact':
                # we are done with all the characters in the word and they matched the current branch
                # now we need to make sure that the current leaf has -1 as a child so that we're sure the word
                # is entirely in the tree and it's not just a prefix of another existing word
                if node_index in current_tree_children:
                    return (-1 in current_tree_children[node_index])
                else:
                    # the node has children though this case should never happen
                    return True
            else:
                # we only want the prefix which at this stage we already found
                return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
obj = Trie()

functions = ["insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search", "search", "search", "search", "search", "search", "search", "startsWith", "startsWith",
             "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]
values = ["app", "apple", "beer", "add", "jam", "rental", "apps", "app", "ad", "applepie", "rest", "jan", "rent", "beer", "jam", "apps", "app", "ad", "applepie", "rest", "jan", "rent", "beer", "jam"]

correct_answer = [None, None, None, None, None, None, False, True, False, False, False, False, False, True, True, False, True, True, False, False, False, True, True, True]

for i in range(0, len(functions)):
    function = functions[i]
    value = values[i]

    if function == 'insert':
        obj.insert(value)
        if correct_answer[i] is None:
            print('correct')
        else:
            print(function + " " + value + " incorrect")
    elif function == 'search':
        if obj.search(value) == correct_answer[i]:
            print('correct')
        else:
            print(function + " " + value + " incorrect")
    elif function == 'startsWith':
        if obj.startsWith(value) == correct_answer[i]:
            print('correct')
        else:
            print(function + " " + value + " incorrect")
