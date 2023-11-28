def esBinario(strbinario):
    return all(digito == '0' or digito == '1' for digito in strbinario)

def BinADecimal(strbinario):
    if esBinario(strbinario):
        decimal = int(strbinario, 2)
        return decimal
    else:
        return None

num_binario = input("Introduce un número binario: ")
resultado_decimal = BinADecimal(num_binario)

if resultado_decimal is not None:
    print(f"El número decimal equivalente es: {resultado_decimal}")
else:
    print("La entrada no es un número binario válido.")
