def split(txt):
    openBrackets=0
    word = ""
    parentheses_List = []
    for x in txt:
        if x not in ["(",")"]:
            return("bad")
    for x in txt:
        if x == "(":
            openBrackets += 1
            word = word + "("
        elif x == ")":
            openBrackets -= 1
            if openBrackets == 0:
                word = word + ")"
                parentheses_List.append(word)
                word = ""
            else:
                word = word + ")"
    return(parentheses_List)
print(split("(())(())(((())))"))
