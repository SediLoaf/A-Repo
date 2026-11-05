import re
def to_spongecase(text):
    textExtraRemoved = re.sub(r'[^A-Za-z]', ' ', text)
    sentence = ""
    j = 0
    for i in range(len(textExtraRemoved)):
        if textExtraRemoved[i] != " ":
            if j % 2 == 1:
                sentence = sentence + textExtraRemoved[i].upper()
            else:
                sentence = sentence + textExtraRemoved[i]
            j += 1
        else:
            sentence = sentence + text[i]
    return(sentence)
print(to_spongecase("who lives in a pineapple under the sea?"))