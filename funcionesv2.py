print("---Funciones version 2---")
print("Sebastian Rojas")
# Zona de listas tuplas set y diccionario
celulares=["Samsung S24 Ultra","Iphone 16 Pro Max","Xiaomi"]
prof=("Benavides","Meza","Nava","Ramirez","Mireles","Quiñones")
# zona de funciones
# Listas
def verlista(Telefonos):
    for uncelular in Telefonos:
        print(uncelular)

# Tuplas
def vertupla(profesores):
    for unprofe in profesores:
        print(unprofe)

# Conjuntos
deportivos={"Porsche","Lamborghini","Ferrari"}

# Diccionario
carro = {
"Marca": "Porsche",
"Modelo": "911",
"Año": 2022
}

# Llamadas a funciones
print("---IMPRIME CELULARES---")
verlista(celulares)

print("---IMPRIME PROFESORES---")
vertupla(prof)

print("---IMPRIME DEPORTIVOS---")
print(deportivos)

print("---IMPRIME CARRO---")
print(carro)
for uncarro in carro:
 print(carro[uncarro])