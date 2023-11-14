
def romanToInt(self, s):
        answer = 0
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        if n == 1: return dict[s[0]]
        for i in range(n):
            if i < n-1 and dict[s[i]] < dict[s[i+1]]:
                answer -= dict[s[i]]
            else :
                answer += dict[s[i]]
        return answer