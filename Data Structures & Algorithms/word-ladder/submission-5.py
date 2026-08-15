class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbors=defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                neighbors[pattern].append(word)
        
        # bfs

        visit=set()
        queue=deque()
        visit.add(beginWord)
        queue.append(beginWord)
        res=1
        while queue:
            for _ in range(len(queue)):
                word=queue.popleft()
                
                if word==endWord:
                    return res
                
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visit:
                            queue.append(neighborWord)
                            visit.add(neighborWord)
            res+=1
        return 0


        

        