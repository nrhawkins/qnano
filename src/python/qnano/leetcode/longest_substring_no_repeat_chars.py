class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        result = 0
        
        chars_seen = dict()
        i = 0
        
        for j in range(0, n):
            
            if s[j] in chars_seen:
                i = max(chars_seen[s[j]], i)

            result = max(result, j-i+1)        
            
            chars_seen[s[j]] = j+1        
            
        return result    
