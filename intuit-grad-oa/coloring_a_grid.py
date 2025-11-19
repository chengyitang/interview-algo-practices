def countPatterns(n):
    """
    計算 n x 3 網格的有效著色方式數量
    
    約束條件：
    - 每行不能全是同一顏色（排除 RRR, GGG, BBB）
    - 每列不能全是同一顏色（所有行在該列都是同一顏色）
    
    返回結果模 10^9 + 7
    """
    MOD = 10**9 + 7
    
    # 生成所有有效的行模式（排除單色行）
    def generate_valid_patterns():
        colors = ['R', 'G', 'B']
        patterns = []
        # 三種顏色都不同：6種排列
        for c1 in colors:
            for c2 in colors:
                for c3 in colors:
                    if c1 != c2 and c2 != c3 and c1 != c3:
                        patterns.append(c1 + c2 + c3)
        # 兩種相同，一種不同：12種
        for c1 in colors:
            for c2 in colors:
                if c1 != c2:
                    patterns.append(c1 + c1 + c2)
                    patterns.append(c1 + c2 + c1)
                    patterns.append(c2 + c1 + c1)
        return patterns
    
    valid_patterns = generate_valid_patterns()
    
    from functools import lru_cache
    
    # 更新列狀態的輔助函數
    def update_col_state(col_state, new_color):
        """
        更新列的狀態
        - '' (未設置) -> 設置為新顏色
        - None (已打破) -> 保持 None
        - 某顏色 -> 如果相同則保持，否則打破為 None
        """
        if col_state == '':
            return new_color  # 第一行，設置為新顏色
        elif col_state is None:
            return None  # 已打破，保持 None
        elif col_state == new_color:
            return new_color  # 繼續保持單色
        else:
            return None  # 打破單色
    
    @lru_cache(maxsize=None)
    def dp(row_idx, col0_color, col1_color, col2_color):
        """
        row_idx: 當前要處理的行索引
        colX_color: 該列目前的顏色（如果所有已處理行都是同一顏色），或 '' 表示未設置，或 None 表示已打破
        """
        if row_idx == n:
            # 所有行處理完，檢查是否有列還是單色（這意味著該列所有行都是同一顏色，違反約束）
            if (col0_color and col0_color != '') or \
               (col1_color and col1_color != '') or \
               (col2_color and col2_color != ''):
                return 0
            return 1
        
        total = 0
        
        for pattern in valid_patterns:
            c0, c1, c2 = pattern[0], pattern[1], pattern[2]
            
            new_col0 = update_col_state(col0_color, c0)
            new_col1 = update_col_state(col1_color, c1)
            new_col2 = update_col_state(col2_color, c2)
            
            total = (total + dp(row_idx + 1, new_col0, new_col1, new_col2)) % MOD
        
        return total
    
    # 初始狀態：所有列都是空字符串（未設置）
    return dp(0, '', '', '')


# 測試
if __name__ == "__main__":
    import sys
    n = int(input().strip())
    result = countPatterns(n)
    print(result)

