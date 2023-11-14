
def lengthOfLastWord(self, s):
        # currLen = 0
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         currLen+=1
        #     if i + 1 == len(s):
        #         return currLen
        #     if s[i] == ' ' and s[i+1] != ' ':
        #         currLen = 0

        # return currLen

        words = s.split()
        if words:
            return len(words[-1])
        return 0