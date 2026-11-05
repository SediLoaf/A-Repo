def staircase(n):
    caseStair = ""
    for x in range(abs(n)) if n<0 else reversed(range(n)):
        caseStair += ("_"*x)+("#"*(abs(n)-x)) + "\n"
    return(caseStair[0:len(caseStair)-1])
print(staircase(-8))

def staircase_recursive(n):
    if type(n) is not list:
        n = [abs(n),abs(n),-1] if n < 0 else [1,n,1]
        return staircase_recursive(n)[:-1]
    else:
        if (n[2] < 0 and not(n[0] > 0)) or (n[2] > 0 and not(n[0] < n[1]+1)): return ""
        n[0] += n[2]
        return "_"*abs(n[1]-(n[0]-n[2]))+((n[0]-n[2])*"#")+"\n"+staircase_recursive(n)
print(staircase_recursive(3))