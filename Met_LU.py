def Met_LU(A,n):
    L=np.zeros((n,n))
    U=np.zeros((n,n))
    for i in range(n):
        L[i, i] = 1

    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i):
                sum=sum+L[i,k]*U[k,j]
            U[i,j]= A[i,j]-sum
    
        for j in range(i+1,n):
            sum=0
            for k in range(i):
                sum=sum+L[j,k]*U[k,i]
            L[j,i] = (A[j,i]-sum)/U[i,i]
    return L,U

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


L, U = Met_LU(A, n)

Z=np.zeros(m)
for i in range(m):
    sum=0
    for k in range(i):
        sum+=L[i][k]*Z[k]
    Z[i]=(B[i]-sum)/L[i][i]

X=np.zeros(m)
for i in range(m-1,-1,-1):
    sum=0
    for k in range(i+1, m):
        sum+=U[i][k]*X[k]
    X[i]=(Z[i]-sum)/U[i][i]


# IMPRESIÓN DE RESULTADOS
print("\nMatriz L:")
for i in range(m):
    print(L[i, :])

print("\nMatriz U:")
for i in range(m):
    print(U[i, :])

print("\nVECTOR SOLUCION X:")
for i in range(m):
    print(f"X({i+1}) = {X[i]}")
