def G_J(A,B,n):
    I = np.eye(n)
    for i in range (n):
        if A[i, i] == 0:
            print("No se puede invertir: pivote cero")
            return None

        piv=1/(A[i,i])
        for j in range(n):
            A[i,j]*= piv
            I[i,j]*= piv  
        B[i]*= piv

        for j in range(n):
            if (not(j==i)):
                mul=A[j,i]
                for k in range(n):
                    A[j,k]= A[j,k]- mul*A[i,k]
                    I[j,k]= I[j,k]-mul*I[i,k]
                B[j] = B[j] - mul * B[i]    
    return B

import numpy as np
m = int(input("Ingresa m: "))
n = m

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

X=G_J(A,B,n)
print(f"Sol: {X}")

