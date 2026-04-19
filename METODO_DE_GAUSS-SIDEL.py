# METODO DE GAUSS-SIDEL
import numpy as np

def Metodo_GS(A,B,Vi, cero=1e-6, max=1000):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n = len(B)

    if Vi is None:
        x = np.zeros(n)
    else:
        x = np.array(Vi, dtype=float)

    cont=0
    for k in range(max):    
        
        x_comp = x.copy()

        for i in range(n):
            suma1 = sum(A[i][j] * x[j] for j in range(i))
            suma2 = sum(A[i][j] * x_comp[j] for j in range(i+1, n))

            x[i]=(B[i]- suma1 - suma2) / A[i][i]

        error = 0.0
        for i in range(n):
            if x[i] != 0:  
                error_por = abs((x[i] - x_comp[i]) / x[i]) * 100
            else:
                error_por = 0

            if error_por > error:
                error = error_por

        print(f"Iteración {k+1}: Solución = {x}, Error = {error:.6f}%")
        cont=k+1

        if error < cero:
            return x,cont
    return x,cont



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

sol_GS, cont_GS = Metodo_GS(A_gs, B_gs, Vi)
print("La solución obtenida por el metodo G-S es el vector:")
print(sol_GS)
print(f"fue obtenida en {cont_GS}° iteraciones") 

