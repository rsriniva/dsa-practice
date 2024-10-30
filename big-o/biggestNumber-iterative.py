sample1Array = [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]


def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    return biggestNumber


print("biggest number in array is ", findBiggestNumber(sample1Array))
