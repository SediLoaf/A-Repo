def remove_duplicates(lst):
    newlst = []
    for x in lst:
        if x not in newlst:
            newlst.append(x)
    return(newlst)

def freq_count(lst:list, el, recur = 0):
    frequencyLst = []
    for x in lst:
        if type(x) == list:
            frequencyLst += freq_count(x,el,recur+1)
        else:
            frequencyLst.append([recur,lst.count(el)])
    if recur == 0:
        frequencyLst = sorted(remove_duplicates(frequencyLst),key=lambda a: a[0])
        maxLayer = frequencyLst[-1][0]
        frequencyList = []
        for x in range(maxLayer+1):
            total = 0
            for y in frequencyLst:
                if y[0] == x:
                    total += y[1]
            frequencyList.append([x,total])
        return(frequencyList)
    return(frequencyLst)
print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2))
