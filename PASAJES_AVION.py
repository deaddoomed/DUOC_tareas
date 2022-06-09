asientos = ([1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30],
            [31,32,33,34,35,36],
            [37,38,39,40,41,42])

pasajero = ["",0,0,"",0] #NOMBRE,RUT,TELEFONO,BANCO,ASIENTO


#FUNCIONES

def consultar(): #OK
    for i in range(0,7):
        if i == 5:
            print("|_________    _________|")
        if i < 2:
            print("| ",asientos[i][0],asientos[i][1],asientos[i][2],"    ",asientos[i][3],asientos[i][4],asientos[i][5],"|")
        else:
            print("|",asientos[i][0],asientos[i][1],asientos[i][2],"  ",asientos[i][3],asientos[i][4],asientos[i][5],"|")

def mostrar(): #OK
    print("__________________________")
    print("NOMBRE: ",pasajero[0])
    print("RUT: ",pasajero[1])
    print("TELEFONO: ",pasajero[2])
    print("BANCO: ",pasajero[3])
    print("__________________________")
    print("")
    
def datos_pasajero(): #OK
    rut=True
    telefono=True
    pasajero[0]=input("INGRESE SU NOMBRE: ")
    while rut:
        try:
            pasajero[1]=int(input("INGRESE SU RUT (sin CV ni puntos): "))
        except ValueError:
            print("DATO INVALIDO")
        else:
            if pasajero[1]<5000000 or pasajero[1]>25000000:
                print("DATO INVALIDO")
            else:
                rut=False
    while telefono:
        try:
            pasajero[2]=int(input("INGRESE SU TELEFONO: "))
        except ValueError:
            print("DATO INVALIDO")
        else:
            if pasajero[2]<9999999 or pasajero[2]>99999999:
                print("DATO INVALIDO")
            else:
                telefono=False
    pasajero[3]=input("INGRESE SU BANCO: ")
    
def comprar(): #OK
    compra=True
    while compra:
        try:
            asiento=int(input("SELECCIONE SU ASIENTO: "))
        except ValueError:
            print("ASIENTO INVALIDO")
        else:
            if asiento>42 or asiento <1:
                print("ASIENTO INVALIDO")
            else:
                for i in range(0,7):
                    for c in range (0,6):
                        if asientos[i][c]==asiento:
                            if asientos[i][c]=="x":
                                print("ASIENTO NO DISPONIBLE")
                            elif asiento>30:
                                print("ASIENTO VIP")
                                valor=240000
                                asientos[i][c]="x"
                                compra=False
                            else:
                                print("ASIENTO NORMAL")
                                valor=74900
                                asientos[i][c]="x"
                                compra=False                
    if pasajero[3]=="bancoDUOC":
        print("DESCUENTO 15% BANCO DUOC!")
        print("VALOR ANTES: ",valor)
        valor=valor*0.85
    print("VALOR PASAJE: ",valor)
    pasajero[4]=asiento

def anular(asiento): #OK
    opcion=True
    print(asiento)
    while opcion:
        seleccion=input("DESEA ANULAR SU PASAJE? Y/N ")
        if seleccion == "y" or seleccion == "Y":
            for i in range(0,7):
                for c in range (0,6):
                    if asientos[i][c]=="x":
                        asientos[i][c]=asiento
            pasajero[0]= ""
            pasajero[1]= 0
            pasajero[2]= 0
            pasajero[3]= ""
            pasajero[4]= 0
            opcion=False
        elif seleccion == "n" or seleccion == "N":
            print("MUCHAS GRACIAS POR SU PREFERENCIA")
            opcion=False
        else:
            print("SELECCION INVALIDA")            

def modificar(): #OK
    dato1= int(input("INGRESE SU ASIENTO"))
    dato2= input("INGRESE SU NOMBRE")
    if dato1 == pasajero[4] and dato2 == pasajero[0]:
        print("VALIDACION EXITOSA!")
        opcion=True
        while opcion:
            print("1.NOMBRE PASAJERO")
            print("2.TELEFONO PASAJERO")
            print("3.CANCELAR")
            seleccion=input("SELECCIONE DATO A MODIFICAR ")
            if seleccion == "1":
                pasajero[0]=input("INGRESE SU NOMBRE: ")
            elif seleccion == "2":
                telefono=True
                while telefono:
                    try:
                        pasajero[2]=int(input("INGRESE SU TELEFONO: "))
                    except ValueError:
                        print("DATO INVALIDO")
                    else:
                        if pasajero[2]<9999999 or pasajero[2]>99999999:
                            print("DATO INVALIDO")
                        else:
                            telefono=False
            elif seleccion == "3":
                opcion=False   
            else:
                print("SELECCION INVALIDA")
    else:
        print("VALIDACION FALLIDA")


#MENU PRINCIPAL

print("____________________________")
print("BIENVENIDO A VUELOS DUOC")
print("")

master=True
while master:
    
    print("1.VER ASIENTOS DISPONIBLES")
    print("2.COMPRAR ASIENTO")
    print("3.ANULAR VUELO")
    print("4.MODIFICAR DATOS DE PASAJERO")
    print("5.SALIR")
    print("")
    menu=input("SELLECCIONE UNA OPCION ")
    
    if menu=="1":
        consultar()
        print("")
        
    elif menu=="2":
        datos_pasajero()
        mostrar()
        comprar()
        print("")

    elif menu=="3":
        anular(pasajero[4])
        mostrar()
        print("")

    elif menu=="4":
        modificar()
        mostrar()
        print("")

    elif menu=="5":   
        print("MUCHAS GRACIAS POR SU PREFERENCIA")
        master=False

    else:
        print("SELECCION INVALIDA") 
