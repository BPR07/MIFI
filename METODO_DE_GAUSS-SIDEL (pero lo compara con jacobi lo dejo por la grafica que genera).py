# METODO DE GAUSS-SIDEL vs Jacobi
import numpy as np
import matplotlib.pyplot as plt

def Metodo_GS(A,B,Vi, cero=1e-6, max=100):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n = len(B)

    if Vi is None:
        x = np.zeros(n)
    else:
        x = np.array(Vi, dtype=float)

    cont=[]
    Val_v=[]
    for k in range(max):    
        
        x_comp = list(x)

        for i in range(n):
            suma1 = sum(A[i][j] * x[j] for j in range(i))
            suma2 = sum(A[i][j] * x_comp[j] for j in range(i+1, n))

            x[i]=(B[i]- suma1 - suma2) / A[i][i]

        cont.append(k)
        Val_v.append(list(x))

        error = 0.0
        for i in range(n):
            if x[i] != 0:  
                error_por = abs((x[i] - x_comp[i]) / x[i]) * 100
            else:
                error_por = 0

            if error_por > error:
                error = error_por

        print(f"Iteración {k}:")
        for i in range(n):
            print(f"V{i+1} = {x[i]:.6f}")
        print(f"Error porcentual = {error:.6f}%")

        if error < cero:
            return x,cont,np.array(Val_v)
    return x,cont,np.array(Val_v)


def jacobi(A,B,Vi=None,cero=1e-6,max=100):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n = len(B)
    if Vi is None:
        x = np.zeros(n)
    else:
        x = np.array(Vi, dtype=float)
    xk1 = np.zeros(n)
    n = len(A)
    for fila in A:
        if len(fila) != n:
            print("la matriz no es cuadrada")

    cont = []
    Val_v = []

    for k in range(max):

        x_comp = x.copy()
        x_k = np.zeros(n)

        for i in range(n):
            suma = sum(A[i][j] * x_comp[j] for j in range(n) if j != i)
            x_k[i] = (B[i] - suma) / A[i][i]

        cont.append(k)
        Val_v.append(list(x_k))

        error = 0.0
        for i in range(n):
            if x_k[i] != 0:
                error_por = abs((x_k[i] - x_comp[i]) / x_k[i]) * 100
            else:
                error_por = 0

            if error_por > error:
                error = error_por

        print(f"Iteración {k}:")
        for i in range(n):
            print(f"V{i+1} = {x_k[i]:.6f}")
        print(f"Error porcentual = {error:.6f}%")

        if error < cero:
            return x_k, cont, np.array(Val_v)
        x = x_k.copy()
    return x, cont, np.array(Val_v)


n= int(input("Tamaño de la matriz de nxn: "))

A_j=[]
A_gs=[]
print("matriz inicial")
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input(f"Valor {i+1},{j+1} = "))
        fila.append(valor)
    A_j.append(fila)
    A_gs.append(fila)

B_j=[]
B_gs=[]
print("Vector solucion")
for i in range(n):
    valor = float(input(f"Valor {i+1} = "))
    B_gs.append(valor)
    B_j.append(valor)

band=int(input("""Tienes vector inicial: 
1) si 
0) no       
"""))
if band==1:
    Vi=[]
    print("Vector inicial: ")
    for i in range(n):
        valor = float(input(f"Valor {i+1} = "))
        Vi.append(valor)
else:
    Vi=None

sol_GS, cont_GS, V_hist_GS = Metodo_GS(A_gs, B_gs, Vi)
print("La solución obtenida por el metodo G-S es el vector:")
print(sol_GS)
print(f"fue obtenida en {len(cont_GS)}° iteraciones") 

print("-------------------------------------------------------------")
sol_J, cont_J, V_hist_J = jacobi(A_j, B_j, Vi)
print("La solución obtenida por el metodo J es el vector:")
print(sol_J)
print(f"fue obtenida en {len(cont_J)}° iteraciones") 



V1_gs = V_hist_GS[:,0]
V2_gs = V_hist_GS[:,1]
V3_gs = V_hist_GS[:,2]

V1_j = V_hist_J[:,0]
V2_j = V_hist_J[:,1]
V3_j = V_hist_J[:,2]

plt.plot(cont_GS, V1_gs, marker='o', color='blue', alpha=0.6)
plt.plot(cont_GS, V2_gs, marker='o', color='blue', alpha=0.6)
plt.plot(cont_GS, V3_gs, marker='o', color='blue', alpha=0.6)

plt.plot(cont_J, V1_j, marker='s', color='red', alpha=0.2)
plt.plot(cont_J, V2_j, marker='s', color='red', alpha=0.2)
plt.plot(cont_J, V3_j, marker='s', color='red', alpha=0.2)



plt.xlabel("Iteraciones")
plt.ylabel("Voltaje")
plt.title("Convergencia - Metodo de Gauss-Seidel vs Jacobi")
plt.legend(["V1_gs","V2_gs","V3_gs","V1_j","V2_j","V3_j"])
plt.grid(True)
plt.show()


