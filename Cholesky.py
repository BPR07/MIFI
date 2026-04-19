
def Matriz_de_L(A, L, m):
    for i in range(m):
        suma = 0
        for k in range(i):
            suma = suma + L[i, k]**2
        
        # Cholesky requiere que el argumento sea positivo
        L[i, i] = math.sqrt(A[i, i] - suma)

        for j in range(i + 1, m):
            suma = 0
            for k in range(i):
                suma = suma + L[j, k] * L[i, k]
            L[j, i] = (A[j, i] - suma) / L[i, i]
    
    return L

# PROGRAMA PRINCIPAL
import numpy as np
import math

m = int(input("¿Cual es el tamaño de tu matriz cuadrada?: "))

A = np.zeros((m, m))
L = np.zeros((m, m))
L_T = np.zeros((m, m))
X = np.zeros(m) 
Y = np.zeros(m)

# LLENADO DEL SISTEMA
for i in range(m):
    for j in range(m):
        A[i, j] = float(input(f"DIME EL NUMERO EN LA POSICION: ({i+1},{j+1}): "))
    X[i] = float(input(f"El {i+1}º valor de tu vector solución (B): "))
    

# COMPROBACIÓN DE MATRIZ SIMÉTRICA
simetria=1
for i in range(m):
    for j in range(m):
        if A[i, j] != A[j, i]:
            print("La matriz no es simetrica")
            simetria=0
            break

    if simetria==0:
        break


if simetria==1:
    L=Matriz_de_L(A, L, m)
    
    # MATRIZ L_T (Transpuesta)
    for i in range(m):
        for j in range(m):
            L_T[i, j] = L[j, i]

    # LY = X
    for i in range(m):
        suma = 0
        for k in range(i):
            suma = suma + (L[i, k] * Y[k])
        Y[i] = (1 / L[i, i]) * (X[i] - suma)

    # (L_T)X = Y 
    for i in range(m - 1, -1, -1):
        suma = 0
        for k in range(i + 1, m):
            suma = suma + (L_T[i, k] * X[k])
        X[i] = (1/L_T[i, i])*(Y[i]-suma)

    # IMPRESIÓN DE RESULTADOS
    print("\nMatriz L:")
    for i in range(m):
        print(L[i, :])

    print("\nMatriz L_T:")
    for i in range(m):
        print(L_T[i, :])

    print("\nVECTOR SOLUCION X:")
    for i in range(m):
        print(f"X({i+1}) = {X[i]}")