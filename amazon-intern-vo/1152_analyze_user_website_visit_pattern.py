class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        """
        {user1:[site1, site2, ...], user2:[site1, site2, site3, ...]}
        """
        users = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)

        patterns = Counter()

        for user, sites in users.items(): # n
            patterns.update(set(combinations(sites, 3)))

        return max(sorted(patterns), key=patterns.get)
    
# Time: O(n) n = len(logs) > len(users)
# Space: O(n) for defaultdict and Counter and sorted patterns
