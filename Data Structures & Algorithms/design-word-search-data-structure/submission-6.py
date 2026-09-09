class TrieNode:
    def __init__(self):
        self.childrens={}
        self.endOfWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root

        for char in word:
            if char not in cur.childrens:
                cur.childrens[char]=TrieNode()
            cur=cur.childrens[char]
        cur.endOfWord=True
        

    def search(self, word: str) -> bool:

        def dfs (i,root):

            cur=root

            for j in range(i,len(word)):
                char=word[j]

                if char==".":
                    for child in cur.childrens.values():
                        if dfs(j+1,child):
                            return True
                    return False
                else:
                    if char not in cur.childrens:
                        return False
                    cur=cur.childrens[char]
            
            return cur.endOfWord 

        return dfs(0,self.root)
        
