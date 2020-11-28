IVA = 0.16

precios_sin_IVA = [415,90,355,385,115,100,250,660]

for precio in precios_sin_IVA:
    resultado = precio * (1 + IVA)
    resultado = round(resultado,2)