import json
import re

#==========================================================================================
def imprimir_dato(texto_a_colocar,dato):
      '''
      imprime un dato por consola.
      recibe como parametro un texto y un dato .
      no tiene retorno.
      '''
      print(texto_a_colocar,dato)
#==========================================================================================
def imprimir_menu_parcial():
        '''
        imprime un menu.
        no tiene parametro.
        no retorna nada .
        
        '''
        imprimir_dato("Menú de opciones:","")
        imprimir_dato("1. Mostrar la lista de todos los jugadores del Dream Team ","")
        imprimir_dato("2. Mostrar estadisticas por indice","")
        imprimir_dato("3. Guardar estadistica opcion 2 ","")
        imprimir_dato("4. Buscar un jugador por su nombre y mostrar sus logros,","")
        imprimir_dato("5. Mostrar el promedio de puntos por partido de todo el equipo del Dream Team","")
        imprimir_dato("6. mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto","")
        imprimir_dato("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales","")
        imprimir_dato("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo","")
        imprimir_dato("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.","")
        imprimir_dato("10. Mostrar los jugadores que han promediado más puntos por partido que valor ingresado.","")
        imprimir_dato("11. Mostrar los jugadores que han promediado más rebotes por partido que valor ingresado.","")
        imprimir_dato("12. Mostrar los jugadores que han promediado más asistencias por partido que valor ingresado.","")
        imprimir_dato("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.","")
        imprimir_dato("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.","")
        imprimir_dato("15. Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a valor ingresado.","")
        imprimir_dato("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido","")
        imprimir_dato("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.","")
        imprimir_dato("18. Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a valor ingreado.","")
        imprimir_dato("19.Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.","")
        imprimir_dato("20. Ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a valor ingresado.","")
        imprimir_dato("23. #BONUS PUNTO 23 , Guarda ranking en un archivo csv.","")
        imprimir_dato("0. Salir","")


def menu_parcial():
      '''
      imprime el menu principal y le pide al usuario una opcion y la valida con la funcion de 
      validacion de enteros.
      no tiene parametros.
      retnorna la opcion casteada a entero si es posible , sino retorna -1.
      '''
      imprimir_menu_parcial()
      opcion = input("\nIngrese la opción deseada: ")
      if ( validar_entero(opcion) == True):
            return  int(opcion)
      else:
            return -1
#==========================================================================================
def validar_entero(string):
      '''
      valida si un string esta compuesto por enteros usando la tabla ascii.
      recibe un str como parametro.
      retorna true si todo el str esta compuesto por numero, y false si no es asi .
      '''
      flag = None
      for letra in string:
            if (ord(letra)>= 48 and ord(letra)<= 57):
                  flag= True
            else :
                  flag = False
      return flag
#==========================================================================================
lista_punto_3 =[-2]
def app_parcial(lista_heroes,opcion):
      '''
      tiene las opcines con sus respectivas funciones dentro de los if.\n
      recibe una lista como párametro y la opcion a ejecutar.\n
      retorna la accion de la opcion que se a elegido .\n
      '''     
      if (opcion == 1 ):
           mostrar_nombres(lista_jugadores,"posicion")
           
      elif(opcion == 2):
           indice = input("ingresar indice a mostrar :")
           if(validar_entero(indice) == True):
               indice = int(indice)
               modificar_lista(lista_punto_3,indice)
               mostrar_por_indice(lista_jugadores,indice)
           else:
                print("el valor ingresado no es un dato valido")
           
      elif(opcion == 3):
           if(lista_punto_3[0]>=0 and lista_punto_3[0]<len(lista_jugadores)):
               if (guardar_estadistica_por_jugador(lista_jugadores,lista_punto_3[0])== True):
                    print("Se guardo el archivo correctamente")
               else:
                    print("no se pudo guardar el archivo")
           else:
                print("aun no se puede guardar nada")  
               
      elif(opcion == 4):
           nombre = input("ingrese nombre del jugador a mostrar: ")
           if(buscar_por_nombre_y_mostra_logros(lista_jugadores,nombre,"logros")==False):
              print("No se encontro considencia")
          
      elif(opcion == 5):
          mostrar_por_nombre_y_promedio(lista_jugadores,ordenar_por_nombre(listar_nombres(lista_jugadores)),"promedio_puntos_por_partido")
          calcular_promedio(lista_jugadores,"promedio_puntos_por_partido")
           
      elif(opcion == 6):
          nombre = input("ingrese nombre de jugador : ")
          confirmar_si_se_encuentra(lista_jugadores,"Miembro del Salon de la Fama del Baloncesto",nombre)
          
      elif(opcion == 7):
          key = "rebotes_totales"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
          
      elif(opcion == 8):
          key = "porcentaje_tiros_de_campo"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
         
      elif(opcion == 9):
          key = "asistencias_totales"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
         
      elif(opcion == 10):
          numero = input("ingresar el numero parametro")
          buscar_superiores(lista_jugadores,numero,"promedio_puntos_por_partido")
      elif(opcion == 11):
          numero = input("ingresar el numero parametro: ")
          buscar_superiores(lista_jugadores,numero,"promedio_rebotes_por_partido")
        
      elif(opcion == 12):
          numero = input("ingresar el numero parametro: ")
          buscar_superiores(lista_jugadores,numero,"promedio_asistencias_por_partido")
         
      elif(opcion == 13):
          key = "robos_totales"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
         
      elif(opcion == 14):
          key = "bloqueos_totales"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
         
      elif(opcion == 15):
          numero = input("ingresar el numero parametro: ")
          buscar_superiores(lista_jugadores,numero,"porcentaje_tiros_libres")
         
      elif(opcion == 16):
          calcular_promedio_con_menos_uno(lista_jugadores,"promedio_puntos_por_partido")
         
      elif(opcion == 17):
          key = "logros"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
        
      elif(opcion == 18):
          numero = input("ingresar el numero parametro: ")
          buscar_superiores(lista_jugadores,numero,"porcentaje_tiros_triples")
       
      elif(opcion == 19):
          key = "temporadas"
          print("el jugador con mas {0} es : {1}".format(key.replace("_"," "),buscar_mayor(lista_jugadores,key)))
         
      elif(opcion == 20):
          numero = input("ingresar el numero parametro: ")
          ordenar_por_posicion_los_superiores_a_valor(lista_jugadores,numero,"porcentaje_tiros_de_campo")
         
      elif(opcion == 23):
          lista_keys = ["puntos_totales","rebotes_totales","asistencias_totales","robos_totales"]
          dic = (buscar_ranking(lista_jugadores,lista_keys)) 
          if(guardar_archivo_csv_ranking(dic,"rankings","w",lista_keys)== True ):
               print("se guardo el archivo correctamente")
          else:
               print("No se pudo guardar el archivo")

      elif(opcion == 0):
            
            return 0
#===============================================================================================
def ordenar_por_key(lista:list,key:str,sentido:bool=True):
    '''
    esta funcion recibe una lista , un key a ordenar y el sentido y ordena segun esos parametros.\n
    recibe como parametro una lista, key deseado a ordenar y el sentido en booleno.\n
    retorna una lista ordenada.\n
    '''    
    rango_a = len(lista)
    flag_swap = True
    
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        if(sentido == True):
                  for indice_A in range(rango_a):
                        if  lista[indice_A]["estadisticas"][key] <  lista[indice_A+1]["estadisticas"][key] :
                              lista[indice_A], lista[indice_A+1] =  lista[indice_A+1], lista[indice_A]
                              flag_swap = True
        else:
                  for indice_A in range(rango_a):
                        if  lista[indice_A]["estadisticas"][key]  >  lista[indice_A+1]["estadisticas"][key] :
                              lista[indice_A], lista[indice_A+1] =  lista[indice_A+1], lista[indice_A]
                              flag_swap = True     
    return lista
#===============================================================================================
def crear_archivo_json(lista,nombre_archivo):
      '''
      esta funcion guarda los diccionarios en un archivo .json.\n
      recibe como parametro una lista y el nombre a poner al archivo.\n
      no tiene retorno .\n
      '''
      with open("{0}.json".format(nombre_archivo),"w") as archivo:
      
            lista_vacia = []
            for personaje in lista:
                  
                  lista_vacia.append(personaje)
            json.dump(lista_vacia, archivo, indent=4, ensure_ascii=False )
#===============================================================================================
def normalizar_datos(lista:list):
     ''' 
     esta funcion normaliza los datos de una lista(los pasa a numericos).\n
     recibe una lista a normalizar.\n
     retorna la lista normalizada.\n
     '''
     for jugador in lista:
          for dato  in jugador["estadisticas"]:
              jugador["estadisticas"][dato] = float(jugador["estadisticas"][dato])
     return lista
#==========================================================================================
def capitalizar_nombre(string:str):
     '''
     esta funcion toma un string y lo a la primera letra la combierte en mayuscula.\n
     recibe como parametro un string.\n
     retorna un string ya capitalizado.\n
     '''
     lista = re.split(" ",string)
     nuevo_string= ""
     for palabra in lista:
          if (palabra == lista[len(lista)-1]):
               nuevo_string = nuevo_string +""+ palabra.capitalize()
          else:
                nuevo_string = nuevo_string + palabra.capitalize() +" "
     return nuevo_string
#==========================================================================================
def abrir_archivo(ruta:str):
    '''
    esta funcion se encarga de abrir un archivo json y volverlo a cerrar.\n
    toma como parametro la ruta del archivo a abrir.\n
    retorna el contenido del arcivo en una lista.\n

    '''
    with open(ruta,"r") as archivo:
        lista_personajes = []
        lista_personajes = json.load(archivo)
    return lista_personajes
jugadores = abrir_archivo("/home/martin/Documentos/programacion_1/dt.json")
lista_jugadores = jugadores["jugadores"]
#=====================================================================================
def guardar_archivo_csv(lista:list,nombre:str):
    '''
    Esta funcion guarda un arichivo en formato csv.\n
    toma como parametro una lista a guardar y el nombre que tomara el archivo.\n
    retorna true si se pudo guardar y false si no .\n
    '''
    flag = False
    with open("{0}.csv".format(nombre),"w") as file:
          mensaje = ""
          for personaje in lista:
                 if(personaje == lista[len(lista)-1]):
                      mensaje = mensaje + "{0}.".format(personaje)
                 else:
                      mensaje = mensaje + "{0},".format(personaje)
          file.write(mensaje)
          flag = True
    return flag
#=====================================================================================
# 1- Mostrar la lista de todos los jugadores del Dream Team. Con el formato
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta
def mostrar_nombres(lista,key):
    '''
    esta funcion muestra el nombre y la key a deseada.\n
    toma como parametro una lista y la key deseada.\n
    no retorna nada .\n
    '''
    for nombre in lista:
        print("{0} - {1}".format(nombre["nombre"],nombre[key]))
#=====================================================================================
def mostrar_por_nombre_y_promedio(lista_jugadores,lista_dos,key):
      '''
      esta funcion muestra el nombre y la key a deseada dentro de estadisticas.\n
      toma como parametro una lista y la key deseada.\n
      no retorna nada .\n
      '''
      for jugador in lista_dos:
          for nombre in lista_jugadores:
                if (nombre["nombre"]==jugador):
                    print("nombre: {0} -{1}: {2}".format(jugador,key.replace("_"," "),nombre["estadisticas"][key]))
#=====================================================================================,
#2- Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas,
# incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, 
# rebotes totales, promedio de rebotes por partido, asistencias totales, promedio
#  de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo,
# porcentaje de tiros libres y porcentaje de tiros triples.
def mostrar_por_indice(lista:list,indice:int):
    '''
    esta funcion muestra un dato segun el indice en que se encuentra.\n
    toma como parametro una lista y el indice a mostrar.\n
    retorna la lista con los datos.\n
    '''
    lista_estadistica = []
    
    if(indice < len(lista)):
        print("nombre: {0}".format(lista[indice]["nombre"]))
        lista_estadistica.append("nombre: {0}".format(lista[indice]["nombre"]))
        for estadistica in lista[indice]["estadisticas"]:
             print("{0} : {1}".format(estadistica.replace("_"," "),lista[indice]["estadisticas"][estadistica]))
             lista_estadistica.append("{0}: {1}".format(estadistica.replace("_"," "),lista[indice]["estadisticas"][estadistica]))
    else:
        print("Indice fuera de rango")
    return lista_estadistica
 
#=====================================================================================
#3- Después de mostrar las estadísticas de un jugador seleccionado por el usuario, 
# permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. 
# El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
# puntos totales, promedio de puntos por partido, rebotes totales, promedio de 
# rebotes por partido, asistencias totales, promedio de asistencias por partido, 
# robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres
# y porcentaje de tiros triples.
def guardar_estadistica_por_jugador(lista:list,indice:int):
   '''
   esta funcion guarda una lista de datos segun el indice punto 2.\n
   toma como parametro la lista .\n
   retorna true si pudo guardar o false si no .\n
   '''
   return guardar_archivo_csv(mostrar_por_indice(lista,indice),"estadistica_{0}".format(lista[indice]["nombre"]))

#=====================================================================================
#4- Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de 
# la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
def buscar_por_nombre_y_mostra_logros(lista:list,nombre:str,key):
     '''
     esta funcion permite listar cierto key.\n
     toma como parametro una lista , un nombre a listar , y la key de ese nombre a listar.\n
     retorna true si se enctro ese nombre y false si no es asi.\n

     '''
     nombre = capitalizar_nombre(nombre)
     flag = False
     for jugador in lista:
          if(re.search(nombre,jugador["nombre"]) != None ):
               print(jugador["nombre"])
               flag = True
               for logros in jugador[key]:
                    print(logros)
     return flag
#=====================================================================================
#5- Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, 
# ordenado por nombre de manera ascendente. 
def ordenar_por_nombre(lista:list):
    '''
    odena alfabeticamente de manera ascendente la lista de diccionarios por su nombre.\n
    toma como parametro una lista.\n
    retorna la lista ordenada. \n
    '''  
    rango_a = len(lista)
    flag_swap = True
    contador = 0
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        
        for indice_A in range(rango_a):
             contador = 0
             while True:
                if (ord(lista[indice_A][contador]) == ord(lista[indice_A+1][contador])):
                    contador += 1
                else:
                     if  ord(lista[indice_A][contador]) > ord(lista[indice_A+1][contador]):
                       lista[indice_A] ,lista[indice_A+1] = (lista[indice_A+1]) ,(lista[indice_A])
                       flag_swap = True
                     break
     
    return lista
def sumar_dato(lista_jugador,key_A_sumar):
     '''
     esta funcion suma datos de una key a eleccion de un genero a elegir.\n
     toma como parametro una lista , la key a sumar , y el genero.\n
     retorma el acumulador de los datos .\n
     '''
     acumulador  = 0.00
     for personaje in lista_jugador:
               acumulador = acumulador + float(personaje["estadisticas"][key_A_sumar])
     string = "El acumulador de {0} es de {1} :".format(key_A_sumar,acumulador)
     #print(string)
     return  acumulador
def calcular_promedio(lista_jugadores,key_a_promediar):
     '''
     esta funcion promedia la key elegida del genero deseado.\n
     toma como parametro una lista , la key a promediar y el genero a promediar .\n
     retorna el promedio en un string   .\n
     '''
     cantidad = len(lista_jugadores)
     acumulador = sumar_dato(lista_jugadores,key_a_promediar)

     promedio = acumulador / float(cantidad)
     string = "El promedio de la key {0} es de {1}".format(key_a_promediar.replace("_"," "),promedio)
     print(string)
     return promedio
     
#===============================================================================================
def listar_nombres(lista):
     '''
     esta funcion permite listar nombres.\n
     toma como parametro una lista a listar.\n
     retorna una nueva lista solo con nombres.\n '''
     nueva_lista = []
     for jugador in lista:
          nueva_lista.append(jugador["nombre"])

     return nueva_lista
#=====================================================================================
#6- Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del 
# Salón de la Fama del Baloncesto.
def confirmar_si_se_encuentra(lista:list,key,nombre:str):
     '''
     esta funcion permine confirmar si se encuentra el string en la lista.\n
     toma como parametro una lista , un key a encontrar y el nombre a buscar. \n
     retorna true si se encontro y false si no fue asi.\n
     '''
     key = capitalizar_nombre(key)
     nombre = capitalizar_nombre(nombre)
     flag = False
     for jugador in lista_jugadores:
         if(re.search(nombre,jugador["nombre"]) != None ):
            for logro in jugador["logros"]:
                 if(capitalizar_nombre(logro) == key):
                    print("jugador {0} si se encuentra en el salon de la fama".format(jugador["nombre"]))
                    flag = True
     if(flag == False):
          print("no se encontro jugador {0} en salon de la fama ".format(nombre))
     return flag
#=====================================================================================
#7- Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
#8- Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
#9- Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
#13- Calcular y mostrar el jugador con la mayor cantidad de robos totales.
#14- Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
#17- Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
#19- Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
def buscar_mayor(lista:list,key_jugador):
    '''
    esta funcion permite buscar un mayor de un key a eleccion.\n
    toma como parametro una lista y la key a buscar.\n
    retorna el nombre del que tiene el mayor dato encontrado.\n
    '''
    mayor_numero = None
    mayor_nombre =""
    contador = 0
    contador_logros =0 
    key = key_jugador.replace(" ","_")
    for jugador in lista:
         if(key=="logros"):
             contador_logros = 0
             for logro in jugador["logros"]:
                   contador_logros = contador_logros + 1
             if(contador == 0):
                    mayor_numero =  contador_logros
                    mayor_nombre =  jugador["nombre"]
                    contador = 1
             else:
                 if (contador_logros >  mayor_numero):
                     mayor_numero =  contador_logros
                     mayor_nombre =  jugador["nombre"]
         else:       
               if(contador == 0):
                    mayor_numero =  jugador["estadisticas"][key]
                    mayor_nombre =  jugador["nombre"]
                    contador = 1
               else:
                    if (jugador["estadisticas"][key] >  mayor_numero):
                         mayor_numero =  jugador["estadisticas"][key]
                         mayor_nombre =  jugador["nombre"]
    return mayor_nombre
#=====================================================================================
#10- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos 
# por partido que ese valor.
#11- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes
# por partido que ese valor.
#12- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más
# asistencias por partido que ese valor.
#15- Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de 
# tiros libres superior a ese valor.
#18- Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje 
# de tiros triples superior a ese valor.
def buscar_superiores(lista:list,numero_base:int,key):
     '''
     esta funcion perimite buscar quienes superar el numero parametro.\n
     toma como parametro una lista, un numero parametro y la key de lo que
     se quiere buscar los que superan.\n
     retorna un a lista de los que superan.\n'''
     lista_nombres_que_superan = []
     if (numero_base.isdigit()):
        numero = float(numero_base)
        for jugador in lista:
             if (float(jugador["estadisticas"][key]) > numero):
                  lista_nombres_que_superan.append(jugador["nombre"])          
     else:
          print("dato ingresado es incorrecto")
          return -1
     print("los que superan el parametro de {0} de {1} son:".format(numero,key.replace("_"," ")))
     for nombre in lista_nombres_que_superan:
          print(nombre)
     return lista_nombres_que_superan
#=====================================================================================
#16- Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la 
# menor cantidad de puntos por partido.
def buscar_menor(lista:list,key_jugador):
    '''
    esta funcion permite buscar un menor de un key a eleccion.\n
    toma como parametro una lista y la key a buscar.\n
    retorna el nombre del que tiene el menor dato encontrado.\n
    '''
    menor_numero = None
    menor_nombre =""
    contador = 0
    key = key_jugador.replace(" ","_")
    for jugador in lista:
         if(contador == 0):
             menor_numero =  jugador["estadisticas"][key]
             menor_nombre =  jugador["nombre"]
             contador = 1
         else:
              if (jugador["estadisticas"][key] <  menor_numero):
                   menor_numero =  jugador["estadisticas"][key]
                   menor_nombre =  jugador["nombre"]
    return menor_nombre
def calcular_promedio_con_menos_uno(lista_jugadores,key_a_promediar):
     '''
     esta funcion promedia la key elegida del genero deseado.\n
     toma como parametro una lista , la key a promediar y el genero a promediar. \n
     retorna el promedio en un string  . \n
     '''
     nombre_menor = buscar_menor(lista_jugadores,key_a_promediar)
     valor_a_restar = 0
     for jugador in lista_jugadores:
          if (jugador["nombre"] == nombre_menor):
              valor_a_resta = jugador["estadisticas"][key_a_promediar]

     cantidad = len(lista_jugadores) - 1 
     acumulador = sumar_dato(lista_jugadores,key_a_promediar) - valor_a_restar

     promedio = acumulador / float(cantidad)
     string = "el promedio de la key {0} menos el menor del equipo es de {1}".format(key_a_promediar.replace("_"," "),promedio)
     print(string)
     return promedio
     
#=====================================================================================
#20- Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha,
# que hayan tenido un porcentaje de tiros de campo superior a ese valor.
def ordenar_por_posicion_los_superiores_a_valor(lista:list,valor,key):
     '''
     esta funcion permite ordenar por posicion si superan un valor establecido.\n
     toma como parametor una lista , el valor a superar , y la key del valor a superar .\n
     retorna un diccionario con los nombres ordenados por posicion.\n'''
     lista_que_superan = buscar_superiores(lista,valor,key)
     diccionario_ordenado_por_posicion = {}
     for nombre in lista_que_superan:
          for jugador in lista:
               if (nombre == jugador["nombre"]):
                    if (jugador["posicion"] in diccionario_ordenado_por_posicion):
                         diccionario_ordenado_por_posicion[jugador["posicion"]].append(jugador["nombre"])
                    else:
                         lista_auxiliar = []
                         lista_auxiliar.append(jugador["nombre"])
                         diccionario_ordenado_por_posicion[jugador["posicion"]] = lista_auxiliar
     for dic in diccionario_ordenado_por_posicion:
          print("----------------------------------------")
          print("De la posicion {0} los jugadores son:".format(dic))
          for jugador in diccionario_ordenado_por_posicion[dic]:
               print("- {0}".format(jugador))
     print("----------------------------------------")     
     return diccionario_ordenado_por_posicion
#=====================================================================================
def modificar_lista(lista_a_modificar,numero):
     '''
     esta funcion permite modificar una lista.\n
     toma como parametro la lista y el nuevo dato.\n
     retorna la lista modificada.\n'''
     lista_a_modificar[0]= numero
     return lista_a_modificar
#=====================================================================================
#BONUS PUNTO 23
def buscar_ranking(lista_jugadores,keys:list):
    '''
    esta funcion perite buscar y ordenar a los jugadores con sus rankings.\n
    toma como parametro lista a rankiar y la lista de keys .\n
    retorna un diccionaro con los jugadores y sus rankings.\n
    '''
    contador_posicion = 0
    lista_keys = keys
    dic_ranking = {}
    for keys in lista_keys:
        print("================================================")
        lista = ordenar_por_key(lista_jugadores,keys,False)
        for jugador in lista_jugadores:
            contador_posicion = 0
            for nombre in lista:
                contador_posicion += 1
                if(nombre["nombre"] == jugador["nombre"]):
                    string = "ranking n° {0}".format(contador_posicion)
                    if (nombre["nombre"] in dic_ranking):
                         dic_ranking[nombre["nombre"]].append(string)
                    else:
                         lista_auxiliar = []
                         lista_auxiliar.append(string)
                         dic_ranking[nombre["nombre"]] = lista_auxiliar
                    break
    return dic_ranking
def guardar_archivo_csv_ranking(lista:list,nombre:str,metodo:str,keys:list):
    '''
    esta funcion perite guardar los datos , con un encabezado.\n
    toma como parametro una lista, el nombre que recibira el archivo , el metodo de apertura de archivo
    y la lista de rankings a guardar.\n
    retorna true si se pudo guardar o false si no fue asi .\n
    '''
    flag = False
    with open("{0}.csv".format(nombre),metodo) as file:
          lista_encabezado = keys
          mensaje_encabezado ="Jugador,"
          mensaje = ""
          for parte in lista_encabezado:
                        mensaje_encabezado =  mensaje_encabezado + "{0},".format(capitalizar_nombre(parte).replace("_"," "))
          for personaje in lista:
                 mensaje = mensaje +"\n" +personaje+","
                 for logros in lista[personaje]:
                        mensaje =mensaje + "{0},".format(logros)
          file.write(mensaje_encabezado)
          file.write(mensaje)
          flag = True
    return flag
#=====================================================================================
