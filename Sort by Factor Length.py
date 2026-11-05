def factorise(n):
    factorList = len([i for i in range(1,n+1) if n % i==0])
    return(factorList)
def factor_sort(nums):
    factorList = [factorise(x) for x in nums]
    aList = []
    for x in range(len(nums)):
        aList.append([nums[x],factorList[x]])
    for i in range(len(aList)):
        for j in range(0, len(aList)-i-1):
            if aList[j][1] == aList[j+1][1]:
                if aList[j][0] < aList[j+1][0]:
                    aList[j], aList[j+1] = aList[j+1], aList[j]
            elif aList[j][1] < aList[j+1][1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
    aList = [x[0] for x in aList]
    return(aList)
print(factor_sort([15, 8, 2, 3]))
