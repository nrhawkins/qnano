class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        
        i, j = 0, 0
        
        while i < len(p) and j < len(s):
            
            if p[i] == ".":
                
                i += 1
                j += 1
                
            elif p[i] == "*":
                
                if i == 0:
                    return False

                elif p[i-1] == s[j]:
                    j += 1
                    
                else:
                    i += 1
                    
            else:
                if p[i] != s[j]: 
                   
                    if i < len(p)-1 and p[i+1] == "*":
                        i += 2                        
                            
                    else:
                        return False
                    
                else:
                    i += 1
                    j += 1

        print(i, j)
                    
                    
        if j < len(s)-1 or i < len(p)-1:
            return False

        else:        
            return True
