import numpy as np

def jacobi(A,B,Vi=None,Cero=1e-6,maximo=100):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    n = len(B)

    if Vi is None:
        xk = np.zeros(n)
    else:
        xk = np.array(Vi, dtype=float)

    xk1 = np.zeros(n)

    n = len(A)
    for fila in A:
        if len(fila) != n:
            print("la matriz no es cuadrada")

    for k in range(maximo):
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * xk[j]
            xk1[i]=(B[i] - suma)/A[i,i]

        error = 0.0

        for i in range(n):
            diferencia = abs(xk1[i] - xk[i])
            if diferencia > error:
                error = diferencia

        if error < Cero:
            return xk1

        xk = xk1.copy()
    return xk1

n = int(input("Ingresa n: "))

A = []
print("matriz inicial")
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input(f"Valor {i+1},{j+1} = "))
        fila.append(valor)
    A.append(fila)

B = []
print("Vector solucion")
for i in range(n):
    valor = float(input(f"Valor {i+1} = "))
    B.append(valor)

solucion = jacobi(A,B)
print(solucion)
