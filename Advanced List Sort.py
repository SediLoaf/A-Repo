def advanced_sort(lst):
    containerList = []
    usedItems = []
    for x in lst:
        if x not in usedItems: containerList.append([y for y in lst if y==x]);usedItems.append(x)
    return(containerList)
print(advanced_sort([2,1,3,4,5,1,2,3,4,5,5,5,2,3,2,1,1,1]))