def to_realNumber(string:str):
    try: return(int(string.split("/")[0])/int(string.split("/")[1]))
    except Exception: return int(string)

def simplify(txt:str):
    fractionList = [int(x) for x in txt.split("/")]
    factorise = lambda num: [x for x in range(1,num+1) if num%x==0]
    try: commonFactor = [x for x in factorise(fractionList[0]) if x in factorise(fractionList[1])][-1] 
    except IndexError: commonFactor = factorise(fractionList[1])[-1]
    fractionList = [str(int(x/commonFactor)) for x in fractionList]
    return("{}/{}".format(*fractionList))

def farey(n):
    return sorted((lambda lst: [item for i,item in enumerate(lst) if item not in lst[:i]])((lambda n: [simplify(y) for y in [f"{numer}/{domer}" for domer in range(1,n+1) for numer in range(domer+1)]])(n)),key=to_realNumber)
print(farey(4))