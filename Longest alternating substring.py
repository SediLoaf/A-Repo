def longest_substring(digits:str):
    if len(digits) < 3:
        return(digits)
    substrings = []
    substring = ""
    prevAlternator = None
    for x in range(len(digits)):
        even_odd = int(digits[x])%2
        if prevAlternator == even_odd:
            if len(substring) > 1: 
                substrings.append(substring)
            substring = ""
        substring += digits[x]
        prevAlternator = even_odd
    substrings.append(substring)
    substrings = sorted(substrings, key=lambda a: len(a))
    return([x for x in substrings if len(x) == len(substrings[-1])][0])
longest_substring("225424272163254474441338664823")
