#FUNCIONES LAMBDA: son funciones anonimas o funciones cortas, se crean para generar procesos rapidos, para definirlas no es necesario usar la palabra def.
#no es recomendable usar estructuras de control.

"""
sintaxis:
lambda argumento(s): expresion
"""

#calcular el cubo de un numero
cubo = lambda x: x**3
print(cubo(3))

#filtrar de una lista numerica solo los numeros impares.

#opc 1. sin funcion
lista = [1,2,3,4]
impares = []
for i in range(len(lista)):
    numero = lista[i]
    if numero % 2 != 0:
        impares.append(numero)

print(impares)
        

#opc 2. funcion tradicional
def impares(lista = []):
    imp = []
    for i in range(len(lista)):
        numero = lista[i]
        if numero % 2 != 0:
            imp.append(numero)
    return imp

listanumeros = []
tamañolista = int(input("Ingrese la cantidad de numero a registrar: "))
cont = 0
while cont < tamañolista:
    numero = int(input("Ingrese el nuemero a registrar en la lista: "))
    listanumeros.append(numero)
    cont=cont+1

print("Lista numeros impares:" , impares(listanumeros))

#opc lambda
lista = [10,11,1,2,3,4,5,6,7,8,9,100,112]

impares = list(filter(lambda C: C%2 != 0, lista))
print(impares)