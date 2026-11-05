def id_mtrx(n):
    try: 
        int(n)
        if n < 0:
            length = int(str(n)[1:])
            negative = True
        elif n >= 0:
            length = n
            negative = False
    except TypeError and ValueError:
        return("Error")
    MatrixContainer = []
    for i in range(length):
        Matrix = []
        for j in range(length):
            if negative:
                if len(Matrix) != i:
                    Matrix.insert(0,0)
                else:
                    Matrix.insert(0,1)
            else:
                if len(Matrix) != i:
                    Matrix.append(0)
                else:
                    Matrix.append(1)
        MatrixContainer.append(Matrix)
    return(MatrixContainer)
for x in id_mtrx(-9):
    print(x)