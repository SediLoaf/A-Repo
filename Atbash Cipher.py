def atbash(txt):
    abcs = list('abcdefghijklmnopqrstuvwxyz')
    sentence = ""
    for letter in txt:
        if letter.lower() not in abcs: 
            sentence += letter
        else:
            if letter in abcs:
                sentence += abcs[(0-(1+abcs.index(letter)))]
            else:
                sentence += abcs[(0-(1+abcs.index(letter.lower())))].upper()
    return(sentence)
print(atbash(""))