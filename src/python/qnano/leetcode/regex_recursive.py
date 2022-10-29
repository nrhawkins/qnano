def isMatch(self, s: str, p: str) -> bool:
        
        print(s, p)
        
        # when pattern runs out, or doesn't exist
        if not p:
            # return False if s still exists, else True if no more s
            return not s

        # compare first char of s and p, if match or p is dot, True, else False
        first_match = bool(s) and p[0] in {s[0], "."}

        # If there's a next char in p and the next char is a *
        if len(p) >= 2 and p[1] == "*":
            # 
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        
        # Not dealing with a * here, so we can move onto the next position
        else:
            print("else")
            return first_match and self.isMatch(s[1:], p[1:])   
