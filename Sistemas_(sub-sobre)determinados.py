####################### METODO DE GAUSS-JORDAN#######################
def G_J(A,n):
    I = np.eye(n)
    for i in range (n):
        if A[i, i] == 0:
            print("No se puede invertir: pivote cero")
            return None

        piv=1/(A[i,i])
        for j in range(n):
            A[i,j]*= piv
            I[i,j]*= piv  

        for j in range(n):
            if (not(j==i)):
                mul=A[j,i]
                for k in range(n):
                    A[j,k]= A[j,k]- mul*A[i,k]
                    I[j,k]= I[j,k]-mul*I[i,k]


    return I

#######################SISTEMA SOBREDETERMINADO#######################
def sis_sobd(A,B,m,n):
    A_t= np.zeros((n,m))
    ATxA=np.zeros((n,n))
    ATxB = np.zeros((n))
    X=np.zeros((n))
    for i in range(m):
        for j in range(n):
            A_t[j][i] = A[i][j]
    
    for i in range(n):
        for j in range(n):
            for k in range(m):
                ATxA[i][j] = ATxA[i][j] + A[k][j] * A_t[i][k]

    for i in range(n):
        for k in range(m):
            ATxB[i] += A_t[i][k] * B[k]
    

    M_I=G_J(ATxA,n)
    if M_I is None:
        return

    for i in range(n):
        for j in range(n):
            X[i] = X[i]+ M_I[i][j] * ATxB[j]

    print("Solución para este sistema sobredeterminado:")
    print(X)

#######################SISTEMA SUBDETERMINADO#######################
def sis_subd(A,B,m,n):
    A_t= np.zeros((n,m))
    AxAT=np.zeros((m,m))
    M_IxB=np.zeros((m))
    X=np.zeros((n))

    for i in range(m):
        for j in range(n):
            A_t[j][i] = A[i][j]
    
    for i in range(m):
        for j in range(m):
            for k in range(n):
                AxAT[i][j] += A[i][k] * A_t[k][j]

    M_I=G_J(AxAT,m)
    if M_I is None:
        return

    for i in range(m):
        for j in range(m):
            M_IxB[i] = M_IxB[i] + M_I[i][j] * B[j]

    for i in range(n):
        for j in range(m):
            X[i] = X[i]+ A_t[i][j] * M_IxB[j]

    print("Solución para este sistema subdeterminado:")
    print(X)

####################### CODIGO PRINCIPAL #######################
import numpy as np
m = int(input("Ingresa m: "))
n = int(input("Ingresa n: "))

A = []
print("matriz inicial")
for i in range(m):
    fila = []
    for j in range(n):
        valor = float(input(f"Valor {i+1},{j+1} = "))
        fila.append(valor)
    A.append(fila)
A = np.array(A)

B = []
print("Vector solucion")
for i in range(m):
    valor = float(input(f"Valor {i+1} = "))
    B.append(valor)
B = np.array(B)
if (m>n):
    sis_sobd(A, B, m, n)
else:
    sis_subd(A, B, m, n)