def shift_sentence(txt):
    txt = txt.split(" ")
    if len(txt) == 1: return(txt[0])
    txtFL = [txt[x][0] for x in range(-1,len(txt)-1)]
    txtRL = [x[1:] for x in txt]
    txt = list(zip(txtFL,txtRL))
    return(" ".join(["".join(x) for x in txt]))
print(shift_sentence("apples are fruits"))