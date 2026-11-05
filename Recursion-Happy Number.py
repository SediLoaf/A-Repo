def is_happy(n):
    if n == 4:
        return(False)
    elif n == 1:
        return(True)
    total = 0
    for x in str(n):
        total += int(x)**2
    return(is_happy(total))
