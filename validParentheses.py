class Solution(object):
    def isValid(self, s):
        valid = '() [] {}'
        if len(s) < 2:
            return False
        if (len(s) == 2) and (s in valid):
            return True
        elif (len(s) == 2) and (s not in valid):
            return False
        else: 
            for i in range(len(s)):
                if (s[i] + s[i+1] in valid):
                    s_new = s.replace(s[i] + s[i+1], '', 1)
                    return self.isValid(s_new)

ob = Solution()
print(ob.isValid('{[({[]})]}{}[]()({})'))
print(ob.isValid('{[({[]})]}{}[]()('))
