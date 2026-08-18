class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endOfWord=True

    def search(self, word: str) -> bool:

        def dfs(j,root):
            cur=root

            # processing word from position j
            for i in range(j,len(word)):

                c=word[i]

                # . means any character
                if c==".":
                    # every possible child
                    for child in cur.children.values():
                        # remaming chars
                        if dfs(i+1,child):
                            return True
                    
                    return False

                else:
                    if c not in cur.children:
                        return False

                    cur=cur.children[c]
            # all the chars matched , check if it actually is a complete word 
            return cur.endOfWord
        
        return dfs(0,self.root)


        
