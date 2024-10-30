sample1Array = [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]

def findMaxNumRec(sampleArray, n):
    if n == 1:
       return sampleArray[0]
    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))

print("biggest number is array is ", findMaxNumRec(sample1Array,len(sample1Array)))