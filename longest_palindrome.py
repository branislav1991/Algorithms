def longestPalindrome(s: str) -> str:
    dp = [[0]*len(s) for _ in s]
    
    max_palin = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if (j-i) == 1:
                if len(max_palin) == 0:
                    max_palin = s[i]
            elif s[i:j] == s[i:j][::-1]: # is palindrom
                if len(s[i:j]) > len(max_palin):
                    max_palin = s[i:j]
                    
    return max_palin

print(longestPalindrome("bb"))