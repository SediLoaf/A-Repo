def simplify(txt):
    #split the text into the two numbers
    fractionList = txt.split("/")
    #Convert the text into int
    fractionList = [int(x) for x in fractionList]
    #check if the two numbers create an int when divided together
    if int(fractionList[0] % fractionList[1]) == 0:
        return(str(int(fractionList[0] / fractionList[1])))
    #else, find the factors of both numbers
    FactorList = [[x for x in range(1,fractionList[0]+1) if fractionList[0] % x==0],
                  [x for x in range(1,fractionList[1]+1) if fractionList[1] % x==0]]
    #find the HCF between the two numbers
    for x in FactorList[0]:
        if x in FactorList[1]:
            commonFactor = x
    #divide both numbers by the commonFactor
    fractionList = [str(int(x/commonFactor)) for x in fractionList]
    #join the numbers together to make it a string fraction again
    fraction = fractionList[0] + "/" + fractionList[1]
    return(fraction)
print(simplify("84/43"))
