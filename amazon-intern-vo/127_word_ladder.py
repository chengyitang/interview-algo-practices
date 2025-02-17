class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        # create adjacency list {pattern:[neighbors]}, time: O(n * m^2)
        neiMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:] # replace i with * to represent a pattern
                neiMap[pattern].append(word)
        

        # BFS, time: O()
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1 # at least one
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in neiMap[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            res += 1
        return 0

# Hard
# Graph, BFS
# Time: O(n * m^2) reason: 
# Space: O(n * m)