#!/usr/bin/env python

#Variables
host = 'localhost'
port = 8050
table= [" "]*9
turno = "cliente"
#Se importa el módulo
import socket, pickle
from interface import*
from logic import *
import ast, cv2

 
#Creación de un objeto socket (lado cliente)
obj = socket.socket()
 
#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
serverRes = True
flag = True
flag1 = True
mens = 0
empate = False
#Creamos un bucle para retener la conexion
while True:
    while flag:
        if Drawn(table) == True :
            flag = False
            empate = True
            print("Dran 1")
        elif flag1 == True: 
            square = random.randint(0,8)
            table[square] = "X"
            data_string = pickle.dumps(table)
            obj.send(data_string)
            print("primer movimiento")
            flag1 = False
        
        #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
        mensajeServidor = obj.recv(1024)
        data_arr = pickle.loads(mensajeServidor)
        data_arr = repr(data_arr)
        data_arr2 = ast.literal_eval(data_arr)
        #Con el método send, enviamos el mensaje
        print("Recibido: ", data_arr)
        table = data_arr2
        print(type(table))
        #print(table)
        
        if flag1 == False:
            print("CLinete inte")
            square = inteligentMoves(table, "X", "O")
            table[square] = "X"
            data_string = pickle.dumps(table)
            obj.send(data_string)
            print("respuesta cliente")
            if win(table, "X"):
                print("Gana Client")
                flag = False
        print("CLinete doble")
        
        #print(mensajeServidor)
    print("FIn CLiente")
    break
#Cerramos la instancia del objeto servidor
obj.close()
change(table)
interfaceTable()
#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")