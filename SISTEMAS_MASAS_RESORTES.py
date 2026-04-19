#------------SISTEMAS MASAS RESORTES-------------------#

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

def mul_mat(A,B):
    n, m = A.shape
    C = np.zeros((m, n))
    for i in range(n):
        for j in range(m):
            suma = 0
            for k in range(m):
                suma += A[i, k] * B[k, j]
            C[i, j] = suma
    return C

def Mat_T(A):
    n, m = A.shape
    C = np.zeros((m, n))
    for i in range(n):
        for j in range(m):
            C[j, i] = A[i, j]
    return C

def Mat_inv_por_GJ(A):
    n=A.shape[0]
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

#------------- Proceso de ortonormalización ---------------------#
def ortonormalizacion(base):
    n, m = base.shape
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
def Metodo_QR(A):
    A_c=A
    for k in range(300):
        Q= ortonormalizacion(A_c)
        Q_t= Mat_T(Q)
        R= mul_mat(Q_t,A_c)
        A_c= mul_mat(R,Q)
    return (A_c)


#------------- llenado del sistema masas-resortes -------------------#
import numpy as np
n =int(input("Cuantas masas tiene tu sistema?: "))
masas = []
for i in range(n):
    masas.append(float(input(f"m{i+1} = ")))

M = np.zeros((n, n))
for i in range(n):
    M[i, i] = masas[i]

# ----------- MATRIZ K PARA SISTEMA MASA-RESORTE -----------

K = np.zeros((n, n))

tipo = int(input("¿Sistema con 1 o 2 paredes?: "))

if tipo == 1:
    k = [float(input(f"k{i+1} = ")) for i in range(n)]

    for i in range(n):
        if i == 0:
            K[i,i] = k[0] + k[1]
        elif i == n-1:
            K[i,i] = k[n-1]
        else:
            K[i,i] = k[i] + k[i+1]

        if i > 0:
            K[i,i-1] = -k[i]
        if i < n-1:
            K[i,i+1] = -k[i+1]

elif tipo == 2:
    k = [float(input(f"k{i+1} = ")) for i in range(n+1)]

    for i in range(n):
        K[i,i] = k[i] + k[i+1]

        if i > 0:
            K[i,i-1] = -k[i]
        if i < n-1:
            K[i,i+1] = -k[i+1]

else:

    print("Error: solo puedes elegir 1 o 2 paredes")
    exit()

M_i =Mat_inv_por_GJ(M)
A =mul_mat(M_i, K)

A_final =Metodo_QR(A)

print("\n--- Matriz final ---")
print(A_final)
print("\n--- Frecuencias naturales ---")
for i in range(n):
    lambda_i = A_final[i, i]
    omega = lambda_i**0.5
    print(f"w{i+1} = {omega:.4f} rad/s")
    f= omega/(2*np.pi)
    print(f"f{i+1} = {f:.4f} Hz")

