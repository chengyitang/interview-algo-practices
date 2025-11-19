def solve_three_parrots(s1, s2, s3):
    """
    解決三隻鸚鵡問題
    
    每隻鸚鵡最多說錯一個字母，找出它們想說的共同單詞。
    
    返回:
    - 如果只有一個可能的單詞，返回該單詞
    - 如果不存在這樣的單詞，返回 "Impossible"
    - 如果有多個可能的單詞，返回 "Ambiguous"
    """
    n = len(s1)
    
    # 檢查長度是否相同
    if len(s2) != n or len(s3) != n:
        return "Impossible"
    
    # 第一步：構建一個候選目標單詞
    # 對於每個位置，使用多數投票原則
    candidate = []
    ambiguous_positions = []  # 記錄可能有多種選擇的位置
    
    for i in range(n):
        chars = [s1[i], s2[i], s3[i]]
        
        # 如果三個字符都相同
        if chars[0] == chars[1] == chars[2]:
            candidate.append(chars[0])
        # 如果有兩個相同
        elif chars[0] == chars[1]:
            candidate.append(chars[0])
            ambiguous_positions.append(i)  # 也可以選擇 chars[2]
        elif chars[0] == chars[2]:
            candidate.append(chars[0])
            ambiguous_positions.append(i)  # 也可以選擇 chars[1]
        elif chars[1] == chars[2]:
            candidate.append(chars[1])
            ambiguous_positions.append(i)  # 也可以選擇 chars[0]
        else:
            # 三個都不同，不可能
            return "Impossible"
    
    candidate_word = ''.join(candidate)
    
    # 檢查候選單詞是否有效（每個輸入最多差1個字符）
    def is_valid(target):
        diff1 = sum(1 for i in range(n) if s1[i] != target[i])
        diff2 = sum(1 for i in range(n) if s2[i] != target[i])
        diff3 = sum(1 for i in range(n) if s3[i] != target[i])
        return diff1 <= 1 and diff2 <= 1 and diff3 <= 1
    
    if not is_valid(candidate_word):
        return "Impossible"
    
    # 檢查是否存在其他有效的目標單詞（多解情況）
    # 使用 backtracking：可能需要同時改變多個 ambiguous 位置才能形成另一個有效解
    # 例如：單獨改變任何一個位置可能無效，但同時改變兩個位置可能有效
    
    # 記錄每個 ambiguous 位置的替代字符
    alternatives = {}
    for pos in ambiguous_positions:
        chars = [s1[pos], s2[pos], s3[pos]]
        current_char = candidate_word[pos]
        # 找出少數字符（替代選項）
        for char in chars:
            if char != current_char:
                alternatives[pos] = char
                break
    
    # 使用 backtracking 查找其他有效解
    def find_other_solution(pos_idx, current_word):
        """
        遞歸查找其他有效解（backtracking）
        嘗試所有可能的 ambiguous 位置組合
        """
        if pos_idx >= len(ambiguous_positions):
            # 已處理完所有 ambiguous 位置
            if current_word != candidate_word and is_valid(current_word):
                return True
            return False
        
        pos = ambiguous_positions[pos_idx]
        
        # 選項1：保持當前字符（多數字符）
        if find_other_solution(pos_idx + 1, current_word):
            return True
        
        # 選項2：使用替代字符（少數字符）
        alt_word = list(current_word)
        alt_word[pos] = alternatives[pos]
        if find_other_solution(pos_idx + 1, ''.join(alt_word)):
            return True
        
        return False
    
    if find_other_solution(0, candidate_word):
        return "Ambiguous"
    
    # 如果只有一個解
    return candidate_word


# 主程序
if __name__ == "__main__":
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    
    result = solve_three_parrots(s1, s2, s3)
    print(result)

