def calcular_iva(precio):
  return precio_final=precio*1,19

def descuento(producto,porcentaje):
  valor=producto*(100-porcentaje)/100
  print("el valor final del producto: $",valor)

def imc(peso,altura):
  indice=peso*altura*altura
  if indice>=40:
    print("Obesidad Grado 3")
  elif indice>=35 and indice<40:
    print("Obesidad Grado 2")
  elif indice>=30 and indice<35:
    print("Obesidad Grado 1")
  elif indice>=25 and indice<30:
    print("Sobrepeso")
  elif indice>=18.5 and indice<25:
    print("Adecuado")
  else:
    print("Bajo Peso")


















  
