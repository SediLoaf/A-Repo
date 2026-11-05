codebook ={
1:"Sailing",
2:"the seven seas",
3:"and",
4:"Through",
5:"sails",
6:"rides",
7:"Our sturdy ship",
8:"crashing waves",
9:"strong and brave",
10:"stormy skies",
11:"bold and wise",
12:"Heave ho!",
13:"We are sailing",
14:"rolling seas",
15:"salty spray",
16:"night and day",
17:[12, 12],
18:[13, 2],
19:[17, 18],
20:[19, 19]}
     
sea_shanty = [
[1, 2],
[4, 10, 3, 8],
[7, 6, 9],
[4, 8 , 3, 10],    
[7, 5, 11],
[20],
[4, 14, 3, 15],
[7, 6, 16],
[4, 15, 3, 14],
[7, 5, 2],
[20]]

def seaCoder(Thelist):
    for i in Thelist:
        if type(i) == list:
            for j in i:
                if type(codebook[j]) != list:
                    print(codebook[j],end=" ")
                    continue
                else:
                    seaCoder(codebook[j])
        else:
            if type(codebook[i]) != list:
                print(codebook[i],end=" ")
                continue
            else:
                seaCoder(codebook[i])
        print()
seaCoder(sea_shanty)