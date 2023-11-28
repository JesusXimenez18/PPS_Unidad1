def esBinario(strbinario):
    return all(bit == '0' or bit == '1' for bit in strbinario)

def binario_a_decimal(strbinario):
    if esBinario(strbinario):
        decimal = int(strbinario, 2)
        return decimal
    else:
        return None

numero_binario = input("Introduce un número binario: ")
resultado_decimal = binario_a_decimal(numero_binario)

if resultado_decimal is not None:
    print(f"El número decimal equivalente es: {resultado_decimal}")
else:
    print("La entrada no es un número binario válido.")
