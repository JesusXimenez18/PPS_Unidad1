def estaEnRango(valor, minimo, maximo):
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    return valor in lista

rango_minimo = 1
rango_maximo = 20
lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]


try:
    numero_usuario = int(input(f"Introduce un número del {rango_minimo} al {rango_maximo}: "))
except ValueError:
    print("Error: Ingresa un número válido.")
else:

    if estaEnRango(numero_usuario, rango_minimo, rango_maximo):
        if estaEnLista(numero_usuario, lista_numeros):
            print(f"¡El número {numero_usuario} está en el rango y en la lista!")
        else:
            print(f"El número {numero_usuario} está en el rango, pero no está en la lista.")
    else:
        print(f"El número {numero_usuario} no está en el rango permitido.")
