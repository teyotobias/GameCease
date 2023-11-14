
def reverseWords(self, s):

        strs = s.split()
        strs = strs[::-1]
        return " ".join(strs)


        # strs = s.split() #split the string into an array of words
        # strs = strs[::-1] reverse the array
        # return " ".join(strs) #return the string of reversed array elements joined by a space -> reversed string