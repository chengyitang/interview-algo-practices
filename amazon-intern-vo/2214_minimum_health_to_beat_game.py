class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        # at each level, I'll need enough health (+ armor) to take the damage.
        # health (+armor) - damage[i]> 0 
        # health > damage[i] (-armor)
        # It's always optimal to use armor where you take the most amount of damage 

        max_damage = max(damage)
        armor_used = False
        health = 1
        for i in range(len(damage) - 1, -1, -1):
            if damage[i] == max_damage and not armor_used:
                health += max(damage[i] - armor, 0)
                armor_used = True
                continue
            health += damage[i]
        return health
    
# Medium
# Array, Greedy
# Time: O(n)
# Space: O(1)   