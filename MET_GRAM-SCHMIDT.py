# METODO DE GRAM-SCHMIDT #  

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


#------------- Proceso de ortonormalización ---------------------#
def ortonormalizacion(m,n,base):
    base_ortonormalizada={}
    
    for i in range(m):
        uk= list(base[f"V{i+1}"])

        for j in range(i):
            uj = base_ortonormalizada[f"u{j+1}"]
            mul = producto_punto(uk, uj)
            uk = [uk[k] - mul * uj[k] for k in range(n)]

        n_uk = norma(uk)
        uk = [element / n_uk for element in uk]

        base_ortonormalizada[f"u{i+1}"] = uk
    
    return (base_ortonormalizada)

#----------------Codigo principal------------------------#
# Ingresando de los vectores #
m=int(input("Cuantos vectores tiene tu conjunto?: "))
n=int(input("Cual es el tamaño de tus vectores?: "))

base={}
for i in range(m):
    vector=[]
    for j in range(n):
        valor=float(input(f"Cual es el valor de tu {i+1}° vetor en la posición {j+1}: "))
        vector.append(valor)
    base[f"V{i+1}"]=vector

resultado = ortonormalizacion(m, n, base)
print("\n--- Vectores Ortonormalizados ---")
for k, v in resultado.items():
    print(f"{k}: {[round(x, 4) for x in v]}")


