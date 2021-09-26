#Function to return a list containing the union of the two arrays.
def mergeArrays(self,a,b,n,m):

    # used logic similar to merge sort. To eliminate duplicates we are checking if two consecutive elements are same.
    l = [0]
    i = 0
    j = 0
    while(True):
        if(i >= n and j >= m):
            break
        if(i < n and j < m):
            if(a[i] < b[j]):
                if(l[-1] != a[i]):
                    l.append(a[i])
                i +=1
            elif(a[i] > b[j]):
                if(l[-1] != b[j]):
                    l.append(b[j])
                j +=1
            else:
                if(l[-1] != a[i]):
                    l.append(a[i])
                i +=1
                j +=1
        else:
            if(i >= n):
                if(l[-1] != b[j]):
                    l.append(b[j])
                j +=1
            elif(j >= m):
                if(l[-1] != a[i]):
                    l.append(a[i])
                i +=1
            
    return l[1:]