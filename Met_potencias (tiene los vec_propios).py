
def desplazamiento(A,VA,iteraciones = 300):
    n = len(A)

    A_np = np.array(A, dtype=float)

    B = A_np - VA * np.eye(n)

    B_inv = Inversa(B,n)

    if B_inv is None:
        print("No se pudo aplicar desplazamiento")
        return None, None

    eigenvalor_inv, eigenvector = metodo_potencias(B_inv, iteraciones)

    eigenvalor = VA + 1/eigenvalor_inv

    return eigenvalor, eigenvector

#inversa de una matrz (del codigo de sistemas sub y sobredeterminados)
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

def metodo_potencias(A, iteraciones=300):
    n = len(A)
    
    x = [1.0] * n
    
    for k in range(iteraciones):
        y = [0.0] * n
        
        for i in range(n):
            suma = 0.0
            for j in range(n):
                suma += A[i][j] * x[j]
            y[i] = suma
        
        max_val = max(abs(num) for num in y)
        
        for i in range(n):
            x[i] = y[i] / max_val

    y = [0.0] * n
    for i in range(n):
        suma = 0.0
        for j in range(n):
            suma += A[i][j] * x[j]
        y[i] = suma
        
    for i in range(n):
        if abs(x[i]) > 1e-8:
            eigenvalor = y[i] / x[i]
            break

    return eigenvalor, x
    

#Ingresado de tamaño de matriz
import numpy as np
n = int(input("ingrese el tamaño de la matriz n: "))
A = []
print("matriz inicial")
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input("Valor = "))
        fila.append(valor)
    A.append(fila)


print("Para potencias:")
valor,vector = metodo_potencias(A)
print("Eigenvalor dominante:", valor)
print("Eigenvector:", vector)

print("Para potencias inversas:")
A_np = np.array(A, dtype=float)
I = Inversa(A_np.copy(), n)
print(I)
valor_inv, vector_inv = metodo_potencias(I)

print("Eigenvalor (inversa):", valor_inv)
print("Eigenvector:", vector_inv)

print("Metodo de potencias con desplazamiento:")
VA = float(input("Ingrese el valor de desplazamiento (VA): "))

valor_desplazado, vector_desplazado = desplazamiento(A, VA)

print("Eigenvalor aproximado:", valor_desplazado)
print("Eigenvector:", vector_desplazado)













