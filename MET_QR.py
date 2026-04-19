

def producto_punto(U,V):
    sum=0
    for i in range(len(U)):
        sum+= (U[i]*V[i])
    return sum

def norma(U):
    sum=0
    for element in U:
        sum+= element**2
    sum=sum**(0.5)
    return sum

def mul_mat(m,n,A,B):
    C = np.zeros((m, n))
    for i in range(n):
        for j in range(m):
            suma = 0
            for k in range(m):
                suma += A[i, k] * B[k, j]
            C[i, j] = suma
    return C

def Mat_T(m,n,A):
    C = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            C[j, i] = A[i, j]
    return C

#------------- Proceso de ortonormalización ---------------------#
def ortonormalizacion(m,n,base):
    base_ortonormalizada=np.zeros((n, m))
    
    for i in range(m):
        uk=base[:,i].copy()
        for j in range(i):
            uj = base_ortonormalizada[:,j]
            mul = producto_punto(uk, uj)
            uk =uk - mul * uj

        n_uk = norma(uk)
        base_ortonormalizada[:, i] = uk / n_uk
    return (base_ortonormalizada)

#-----------------------  Q R ---------------------------------#
def Metodo_QR(m,n,A):
    A_c=A
    for k in range(100):
        Q= ortonormalizacion(m, n, A_c)

        Q_t= Mat_T(m,n,Q)
        R= mul_mat(m,n,Q_t,A_c)

        A_c= mul_mat(m,n,R,Q)

    return (A_c)



#------------------ Codigo principal --------------------#
import numpy as np
m=int(input("Cuantas columnas tiene tu matriz?: "))
n=int(input("Cuantas filas tiene tu matriz?: "))

lista=[]
for i in range(m):
    vector=[]
    for j in range(n):
        valor=float(input(f"Cual es el valor de tu matriz en la posición ({i+1},{j+1}): "))
        vector.append(valor)
    lista.append(vector)
Matriz=np.array(lista)

A_f = Metodo_QR(m, n, Matriz)
print("\n--- Matriz final ---")
print(A_f)

print("\n--- Eigenvalores---")
for i in range(n):
    print(f"Eigenvalores {i+1} = {A_f[i,i]}")
