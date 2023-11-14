
def longestCommonPrefix(self, strs):
        answer = strs[0]
        n = len(strs)
        j = 0
        for i in range(1, n):
            currString = strs[i]
            while j < min(len(currString), len(answer)) and currString[j] == answer[j]:
                j+= 1
            answer = answer[0:j]
            j = 0
        return answer