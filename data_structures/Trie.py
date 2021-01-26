class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}

        # occurances of this character in the creation process
        self.counter = 1

        # this node is word's last character?
        self.word_finished = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children.get(char)

            else:
                node.children.update({char:TrieNode(char)})
                node = node.children.get(char)
            
        node.word_finished = True

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                return False
        
        return node.word_finished

    def _get_potentials(self, _str):
        '''will return a list of possible words given a string _str'''
        pass


    def __repr__(self):
        pass



if __name__ == '__main__':
    t = Trie()

    t.add_word('help')
    t.add_word('helm')
    t.add_word('hat')

    print(t.search('hel'))