def count_distinct_palindromic_substrings(s):
    """
    計算字符串中所有不同的連續回文子串的數量
    
    使用 expand around centers 方法：
    - 對於每個可能的中心點，向兩邊擴展
    - 處理奇數長度和偶數長度的回文
    
    時間複雜度: O(n^2)
    空間複雜度: O(n^2) 最壞情況（所有子串都是回文）
    """
    n = len(s)
    distinct_palindromes = set()
    
    # 擴展函數：從中心向兩邊擴展，找出所有回文子串
    def expand_around_center(left, right):
        """從 (left, right) 中心向兩邊擴展"""
        while left >= 0 and right < n and s[left] == s[right]:
            # 找到一個回文子串
            palindrome = s[left:right + 1]
            distinct_palindromes.add(palindrome)
            left -= 1
            right += 1
    
    # 遍歷所有可能的中心點
    for i in range(n):
        # 奇數長度的回文：中心在字符上
        # 例如 "aba"，中心在索引 1 的 'b' 上
        expand_around_center(i, i)
        
        # 偶數長度的回文：中心在兩個字符之間
        # 例如 "abba"，中心在索引 1 和 2 之間（即 'b' 和 'b' 之間）
        # 條件 i < n - 1 確保 i+1 不會超出字符串範圍
        # 當 i = n-1 時，i+1 = n，會超出索引範圍 [0, n-1]
        if i < n - 1:
            expand_around_center(i, i + 1)
    
    return len(distinct_palindromes)


# 主程序
if __name__ == "__main__":
    s = input().strip()
    result = count_distinct_palindromic_substrings(s)
    print(result)

