class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # need to build a graph of words that differ by one
        length=len(endWord)
        if beginWord not in wordList:
            wordList.append(beginWord)
        #base case: if endword not in wordList, return
        if endWord not in wordList:
            return 0
        #building an adjacency list
        adj = defaultdict(list)
        hmap=defaultdict(list)

        #cant simply delete a char and store:
        #talk (dlt index 3 ) and tail (dlt index 2): lead to "tal"
        #end up linking together- which is wrong
        #MUST USE WILDCARD
        for word in wordList:
            for char in range(length):
                key=word[:char]+"*"+word[char+1:]
                hmap[key].append(word)
        for keys, values in hmap.items():
            if len(values)>=2:
                for i in range(len(values)):
                    for j in range(i+1,len(values)):
                        adj[values[i]].append(values[j])
                        adj[values[j]].append(values[i])
        
        #bfs to track down  MINIMUM patj start to end
        def bfs(startWord,endWord):
            queue=deque()
            queue.append(startWord)
            visited=set()
            visited.add(startWord)
            distance=1
            while queue:
                for i in range(len(queue)):
                    word=queue.popleft()
                    if word==endWord:
                        return distance

                    for neighbor in adj[word]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                distance+=1
            return 0
        #main - function now to call bfs
        return bfs(beginWord,endWord)
                    
        
