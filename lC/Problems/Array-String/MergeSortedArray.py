
def merge(self, nums1, m: int, nums2, n):
        mergedList = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                mergedList.append(nums1[i])
                i+=1
            else:
                mergedList.append(nums2[j])
                j+=1
        
        while i < m:
            mergedList.append(nums1[i])
            i+=1
        while j < n:
            mergedList.append(nums2[j])
            j+=1
        return mergedList