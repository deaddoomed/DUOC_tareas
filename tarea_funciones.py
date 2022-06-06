selec=True
master=True
datos=True

def calcular_iva(precio):
  precio_final = precio*1.19
  print("el precio con iva es $",precio_final)

def descuento(producto,porcentaje):
  valor=producto*(100-porcentaje)/100
  print("el valor final del producto: $",valor)

def imc(peso,altura):
  indice=peso/(altura*altura)
  print("IMC = ",indice)
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

print("BIENVENIDO A PRUEBA DE FUNCIONES")

while master:
  print("")
  print("1.CALCULAR IVA")
  print("2.CACULAR DESCUENTO")
  print("3.CALCULAR IMC")
  print("4.SALIR")

  while selec:
    try:
      seleccion=int(input("SELECCIONE OPCION= "))
    except ValueError:
      print("SELECCION NO VALIDA")
    else:
      if seleccion<=4 or seleccion>=1:
        datos=True
        selec=False
      else:
        print("SELECCION NO VALIDA")

  if seleccion==1:
    while datos:
      try:
        dato1=int(input("INGRESE EL VALOR SIN IVA "))
      except ValueError:
        print("DATO INVALIDO")
      else:
        if dato1<0:
          print("DATO INVALIDO")
        else:        
          calcular_iva(dato1)
          datos=False
    selec=True
    
  if seleccion==2:
    while datos:
      try:
        dato1=int(input("INGRESE EL VALOR DEL PRODUCTO "))
      except ValueError:
        print("DATO INVALIDO")
      else:
        if dato1<0:
          print("DATO INVALIDO")
        else:
          datos=False
    datos=True
    while datos:
      try:
        dato2=int(input("INGRESE EL DESCUENTO "))
      except ValueError:
        print("DATO INVALIDO")
      else:
        if dato2>100 or dato2<0:
          print("DATO INVALIDO")
        else:
          datos=False
    descuento(dato1,dato2)
    selec=True
    
  if seleccion==3:
    while datos:
      try:
        dato1=int(input("INGRESE EL PESO "))
      except ValueError:
        print("DATO INVALIDO")
      else:
        if dato1<0:
          print("DATO INVALIDO")
        else:
          datos=False
    datos=True
    while datos:
      try:
        dato2=float(input("INGRESE LA ALTURA "))
      except ValueError:
        print("DATO INVALIDO")
      else:
        if dato2<0:
          print("DATO INVALIDO")
        else:
          datos=False            
    imc(dato1,dato2)
    selec=True
    
  if seleccion==4:
    print("HASTA LUEGO")
    master=False
















  
