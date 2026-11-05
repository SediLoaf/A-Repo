def get_quartiles(lst, method):
    median = lambda arr: (arr[(len(arr)//2)] if len(arr)%2==1 else sum([arr[(len(arr)//2)-1],arr[(len(arr)//2)]])/2)
    lst = sorted(lst)
    q0,q2,q4 = lst[0],median(lst),lst[-1]
    mid = len(lst)//2
    if method == "MM":
        q1 = median(lst[:mid])
        q3 = median(lst[(mid+(len(lst)%2==1)):])
    elif method == "T":
        q1 = median(lst[:(mid+(len(lst)%2==1))])
        q3 = median(lst[mid:])
    elif method == "MS":
        side = lambda num,l_r: int(num)-l_r if num-int(num)==0.5 else round(num)-1
        q1 = lst[side((len(lst)+1)/4,0)]
        q3 = lst[side(3*(len(lst)+1)/4,1)]
    return[q0,q1,q2,q3,q4]
print(get_quartiles([1,2,3,4,5,6,7,8],"MS"))