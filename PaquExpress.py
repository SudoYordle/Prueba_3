#PaquExpress

def registro():
    cliente=input("Por favor ingrese el nombre del cliente: ")
    listaDatos["cliente"]=cliente
    direccion=input("Por favor ingrese la dirección del cliente: ")
    listaDatos["direccion"]=direccion
    sector=input("Por favor ingrese el sector del cliente: ")
    listaDatos["sector"]=sector
    pequeno=input("Por favor indique cuantos paquetes pequeños hay en el pedido: ")
    mediano=input("Por favor indique cuantos paquetes medianos hay en el pedido: ")
    grande=input("Por favor indique cuantos paquetes grandes hay en el pedido: ")
    listaDatos["paqPeq"]=pequeno
    listaDatos["paqMed"]=mediano
    listaDatos["paqGra"]=grande
    listaClientes.append(listaDatos)
    return
    

def listarPedidos():
    print(listaClientes)

def imprimirHojaRuta():
    print("PlaceHolder")





#Menu
listaDatos={"cliente":"","direccion":"","sector":"","paqPeq":"","paqMed":"","paqGra":""}
listaClientes=[]
selectOpcion=1


while selectOpcion>0 and selectOpcion<5:
    print("Bienvenido al menu de PaquExpress","1.Registrar pedido","2.Listar todos los pedidos","3.Imprimir hoja de ruta","4.Salir del programa",sep="\n")
    selectOpcion=int(input("por favor elija una opción: "))

    if selectOpcion==1:
        registro()

        
    if selectOpcion==2:
        print("Estos son los datos de los clientes registrados: ")
        listarPedidos()
        
    if selectOpcion==3:
        imprimirHojaRuta()

    if selectOpcion==4:
        print("Muchas gracias por su preferencia")
        break

