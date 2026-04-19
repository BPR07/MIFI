    
def Inversa(A,n):
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

def metodo_potencias(A, iteraciones=50):
    n = len(A)
    
    # Vector inicial (todos unos)
    x = [1.0] * n
    
    for k in range(iteraciones):
        # Multiplicación A*x
        y = [0.0] * n
        
        for i in range(n):
            suma = 0.0
            for j in range(n):
                suma += A[i][j] * x[j]
            y[i] = suma
        
        # Encontrar el valor máximo (para normalizar)
        max_val = max(abs(num) for num in y)
        
        # Normalizar el vector
        for i in range(n):
            x[i] = y[i] / max_val
    
    # El eigenvalor dominante aproximado
    eigenvalor = max_val
    
    return eigenvalor, x


import numpy as np
#Ingresado de tamaño de matriz
n = int(input("ingrese el tamaño de la matriz n: "))
A = []
print("matriz inicial")
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input("Valor = "))
        fila.append(valor)
    A.append(fila)

    
#impresion para valores de potencias
print("Para potencias:")
valor,vector = metodo_potencias(A)
print("Eigenvalor dominante:", valor)
print("Eigenvector:", vector)

print("---------------------------------------------")
#impresion para valores de potencias inversas
print("Para potencias inversas:")
A_np = np.array(A, dtype=float)
I = Inversa(A_np.copy(), n)
print(I)
valor_inv, vector_inv = metodo_potencias(I)

print("Eigenvalor (inversa):", 1/valor_inv)
print("Eigenvector:", vector_inv)