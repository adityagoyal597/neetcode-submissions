class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        curr=self.root

        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            
            curr=curr.children[char]
        
        curr.endOfWord=True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie=Trie()

        for word in wordDict:
            trie.insert(word)

        cache={}
        
        def dfs(i):

            if i ==len(s):
                return True
            
            if i in cache:
                return cache[i]
            
            curr=trie.root

            for j in range(i,len(s)):

                if s[j] not in curr.children:
                    break
                
                curr=curr.children[s[j]]

                if curr.endOfWord:

                    if dfs(j+1):
                        cache[i]=True
                        return True
            cache[i]=False
            return False
        
        return dfs(0)
        