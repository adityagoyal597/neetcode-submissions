class TrieNode:
    def __init__(self):
        self.childrens={}
        self.endOfWord=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        # self.root already defined in prefixTree initialization
        cur=self.root
        for char in word:
            if char not in cur.childrens:
                cur.childrens[char]=TrieNode()
            cur=cur.childrens[char]
        # at the end , endofword=false
        cur.endOfWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        for char in word:
            if char not in cur.childrens:
                return False
            cur=cur.childrens[char]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for char in prefix:
            if char not in cur.childrens:
                return False
            cur=cur.childrens[char]
        return True
        
        