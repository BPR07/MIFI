def Gauss(A,X,Sol,m):
    #Mat_trinagular
    for k in range(m-1):
        for i in range(k+1,m):
            mul=A[i][k]/A[k][k]

            for j in range(k,m):
                A[i][j]=A[i][j]-mul*A[k][j]
            
            X[i]=X[i]-mul*X[k]
    

    #SOL
    Sol[m-1] = X[m-1] / A[m-1][m-1]
    
    for i in range(m - 2, -1, -1):
        sum_val = 0.0
        for j in range(i + 1, m):
          
            sum_val = sum_val + A[i][j] * Sol[j]
        Sol[i] = (X[i] - sum_val) / A[i][i]
    
    return Sol



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

X=[]
print("Vector solucion")
for i in range(m):
    valor = float(input(f"Valor {i+1} = "))
    X.append(valor)
X = np.array(X)
Sol = np.zeros(m)

Sol=Gauss(A,X,Sol,m)
print("Solución del sistema:")
for i in range(m):
    print(f"Variable {i}°= {Sol[i]}")