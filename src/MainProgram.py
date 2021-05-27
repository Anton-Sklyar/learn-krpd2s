
def MatrixMult(A,B,stra,colb,cola):
    if (type(A) != list or type(B) != list):
        raise TypeError("Matrix type Error")
    if (type(stra) != int or type(colb) != int or type(cola) != int):
        raise TypeError("Matrix size type Error")
    if (len(A)== 0 or len(B) == 0):
        raise TypeError("Matrix has one dimension")
    if (stra<1 or colb<1 or cola<1) :
        raise ValueError("Invalid matrix size Error")
    C=[]
    for i in range(stra):
        C.append([])
        for j in range(colb):
            C[i].append(0)
            for k in range(cola):
                C[i][j]+=A[j][k]*B[k][j]
    return C
def MakeMatrix(x,strx,colx):
    if (type(x) != str):
        raise TypeError("Name of Matrix must be a string")
    if (type(strx) != int or type(colx) != int):
        raise TypeError("Matrix size type Error")
    if (strx<1 or colx<1) :
        raise ValueError("Invalid matrix size Error")
    X=[]
    for i in range(strx):
        X.append([])
        for j in range(colx):
            X[i].append(0)
            X[i][j] = int(input(f"{x}[{i + 1}][{j + 1}] = "))
    return X

def MainDialog():
    stra=int(input("Введіть кількість рядків першої матриці "))
    cola=int(input("Введіть кількість стовпців першої матриці "))
    strb=int(input("Введіть кількість рядків другої матриці "))
    colb=int(input("Введіть кількість стовпців другої матриці "))
    if(stra!=colb):
        print("Перемноження неможливе")
        return 0
    a=MakeMatrix('a',stra,cola)
    b=MakeMatrix('b',strb,colb)
    c=MatrixMult(a,b,stra,colb,cola)
    for i in range(len(c)):
        print('\n',c[i])

MainDialog()
