def agregarPasajeros(pasajeros):
    nombre=input("ingrese el Nombre o una (x) para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("ingrese el Nombre o una (x) para cortar: ")
    return pasajeros

 
def agregarCiudades(ciudades):
    ciudad=input("ingrese la Ciudad (x) para cortar: ")
    while ciudad!="x":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("ingrese la Ciudad (x) para cortar: ")
    return ciudades

 
def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

 
def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

 
def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

 
def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad


#programa principal
pasajeros=[]
ciudades=[]
while True:
    print(" ---------------------------------------")
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    print("----------------------------------------")
    opcion=int(input(" <  ACCION A EJECUTAR   > : "))
    
    if opcion==1:
        print("- - - - - - - - - ")
        print("AGREGAR PASAJEROS")
        print("- - - - - - - - - ")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("- - - - - - - - -")
        print("AGREGAR CIUDADES")
        print("- - - - - - - - -")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        print("- - - - - - - ")
        dni=int(input("DNI: "))
        print("- - - - - - - ")
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        print("- - - - - - - -  - - - -")
        ciudad=input("Ciudad a buscar: ")
        print("- - - - - - - - - - - - ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        print("- - - - - - - -")
        dni=int(input("DNI: "))
        print("- - - - - - - -")
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        print("- - - - - - -")
        pais=input("País: ")
        print("- - - - - - ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("ºººººººººººººººººººººººººº")
        print(" ¡¡ OPCION INVALIDA !!")
        print("ºººººººººººººººººººººººººº")
