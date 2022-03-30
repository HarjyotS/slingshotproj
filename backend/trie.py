# Harjyot Sahni 2022


class node:
    def __init__(self):
        # basic children structure, one list value for each letter of the alphabet
        self.children = [None] * 26
        self.leaf = False


class Trie:
    def __init__(self):
        self.base = node()

    # gets the index of the letter in the alphabet
    def identifier(self, ch):
        return ord(ch) - ord("a")

    # insert a word into the trie
    def add_keyword(self, word):
        pointer = self.base
        for level in range(len(word)):
            index = self.identifier(word[level])
            # Check if the letter is already in the trie
            if not pointer.children[index]:
                # if not, create a new node
                pointer.children[index] = node()
            pointer = pointer.children[index]
        # set node leaf value to true to show the end of the word
        pointer.leaf = True

    def search(self, word):
        pointer = self.base
        # if the word is not in the trie, return
        for level in range(len(word)):
            index = self.identifier(word[level])
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        # if the word is in the trie, return true
        return pointer.leaf

    # remove a word from the trie

    def remove(self, word):
        pointer = self.base
        # if the word is not in the trie, return
        for level in range(len(word)):
            index = self.identifier(word[level])
            if not pointer.children[index]:
                return
            pointer = pointer.children[index]
        # if the word is in the trie, remove it
        if pointer.leaf:
            pointer.leaf = False
            return
        # if the word is not a leaf, remove the children
        for i in range(26):
            if pointer.children[i]:
                pointer.children[i] = None

    # search for suggestions with a given prefix
    def suggest(self, prefix):
        pointer = self.base
        # if the prefix is not in the trie, return
        for level in range(len(prefix)):
            index = self.identifier(prefix[level])
            if not pointer.children[index]:
                return []
            pointer = pointer.children[index]
        # if the prefix is in the trie, return all the words with the prefix
        words = []
        self.suggest_helper(pointer, prefix, words)
        return words

    def suggest_helper(self, pointer, word, words):
        # if the node is a leaf, add the word to the list of words
        if pointer.leaf:
            words.append(word)
        for i in range(26):
            if pointer.children[i]:
                self.suggest_helper(
                    pointer.children[i], word + chr(ord("a") + i), words
                )

    # extract all the words in the trie
    def extract_all(self):
        words = []
        self.extract_helper(self.base, "", words)
        return words

    def extract_helper(self, pointer, word, words):
        # if the node is a leaf, add the word to the list of words
        if pointer.leaf:
            words.append(word)
        for i in range(26):
            if pointer.children[i]:
                self.extract_helper(
                    pointer.children[i], word + chr(ord("a") + i), words
                )

    # return the children of the trie recursivly in a dictionary
    def get_children(self, obj):
        paths = {}
        for i in range(26):
            if obj.children[i]:
                paths[chr(ord("a") + i)] = obj.children[i]
        for i in paths:
            print(paths[i])
            paths[i] = self.get_children(paths[i])
        return paths

    def display_trie(self):
        # show the trie in a dictionary format to be exported to clients as a json.
        paths = {}
        for i in range(26):
            if self.base.children[i]:
                paths[chr(ord("a") + i)] = self.base.children[i]

        for i in paths:
            print(paths[i])
            paths[i] = self.get_children(paths[i])
        return paths

    def clear_trie(self):
        self.base = node()


"""
citings
https://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words
https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods
"""


## usage

# obj = Trie()
# obj.add_keyword("geereded")
# obj.add_keyword("geeks")
# obj.add_keyword("geekt")
# obj.add_keyword("card")
# obj.add_keyword("labdso")
# print(obj.search("geek"))
# print(obj.suggest("geedededede"), "ee")

