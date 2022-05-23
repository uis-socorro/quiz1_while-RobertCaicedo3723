print("-------------------------------------------")
print("-------------Negocio-----------------------")
print("-------------------------------------------")


#input

c1 = int(input("Ingrese el capital de Pedro: "))
c2 = int(input("Ingrese el capital de Juan: "))
c3 = int(input("Ingrese el valor de c3: "))

#Procesing

n = 0

while c1+c2<c3:
    c4 = c1+0.03*c1+c2+0.04*c2 
    n = n+1


#Output
print("Los meses que necesitan ambos para iniciar su negocio son: " + str(n))
