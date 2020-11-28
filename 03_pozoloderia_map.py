#How to use map function on Python

IVA = 0.16

def aplicar_iva(precio):
    resultado = precio * (1 + IVA)
    return round(resultado,2)

precios_sin_IVA = [415, 90, 355, 385, 115, 100, 250, 660]
print(precios_sin_IVA)

# Use map in order to apply a function on each element on the list "precios_sin_IVA"
precios_sin_IVA = list(map(aplicar_iva,precios_sin_IVA))
print(precios_sin_IVA)