from typing import List

def findOdd(series: List[str]) -> str:

    all_word_diffs = []

    for word in series:
        word_diffs = []
        for i in range(1, len(word)):
            word_diffs.append(ord(word[i]) - ord(word[i - 1]))
            
        if all_word_diffs == [] or word_diffs in all_word_diffs:
            all_word_diffs.append(word_diffs)
        else:
            return word
                

        
assert(findOdd(["ACB", "BDC", "CED", "DEF"]) == "DEF" )