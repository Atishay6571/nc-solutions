class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.isEnd=True


    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
        
class TrieNode():
    #children havee key value pairs like {character: Node}
    def __init__(self):
        self.isEnd=False
        self.children={}
