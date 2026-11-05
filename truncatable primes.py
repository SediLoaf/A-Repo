def truncatable(n):
    allPrimes = lambda lst: all([(lambda num: len([x for x in range(1,num+1) if num%x==0])==2)(int(x)) for x in lst])
    leftVal = [str(n)[-x:] for x in reversed(range(1,len(str(n))+1))]
    rightVal = [str(n)[:x] for x in reversed(range(1,len(str(n))+1))]
    return {(True,False):"left",(False,True):"right",
            (True,True):"both",(False,False):False
           }.get(((allPrimes(leftVal),allPrimes(rightVal)) if "0" not in str(n) else (False,False)),False)
    
print(truncatable(103))