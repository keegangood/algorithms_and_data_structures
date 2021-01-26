class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = []

        # occurances of this character in the creation process
        self.counter = 1

        # this node is word's last character?
        self.word_finished = False


class Trie:
    def __init__(self):
        head

    def __repr__(self):
        pass

