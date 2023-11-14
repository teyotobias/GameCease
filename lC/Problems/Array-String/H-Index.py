
def hIndex(self, citations):
        #Two different implementations

        # citations.sort()
        citations.sort(reverse=True)

        n = len(citations)
        count = 0

        # for i in range(n):
        #     if citations[i] >= n - i:
        #         count+=1
    
        for i in range(n):
            if citations[i] > i:
                count+=1
    

        return count