def josephus(people):
    arrer = [x for x in range(1,people+1)]
    removal = lambda arr: removal([arr[x] for x in range(len(arr)) if x%2==0] if len(arr)%2==0 else [arr[x] for x in range(len(arr)) if x%2==0 and x!=0]) if len(arr) > 1 else arr[0]
    return(removal(arrer))