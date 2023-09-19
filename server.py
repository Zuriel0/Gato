#!/usr/bin/env python
 
#Se importa el módulo
import socket, pickle
from logic import *
import ast, cv2
from interface import *
 
#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#Puerto y servidor que debe escuchar
ser.bind(("", 8050))
 
#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)
 
#Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()
clientRes = True
flag = True
empate = False
while True:
    while flag:
        #Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
        recibido = cli.recv(1024)
        data_arr = pickle.loads(recibido)
        data_arr = repr(data_arr)
        table = data_arr
        table = ast.literal_eval(table)
        if  Drawn(table):
            flag = False
            empate = True
            print("Bandera de Dranw", flag)
        else:
            square = inteligentMoves(table, "O", "X")
            print(type(table))
            table[square] = "O"
            data_string = pickle.dumps(table)
            cli.send(data_string)
            #print(table)
            print("Rspuesta")
            if win(table, "O"):
                print("Gano Server")
                flag = False
        #Si se reciben datos nos muestra la IP y el mensaje recibido
        print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

        print("Recibido: ", data_arr)
        #Devolvemos el mensaje al cliente
    if empate == True:
        cv2.waitKey(0)
    print("FIn Server")
    break
#Cerramos la instancia del socket cliente y servidor
cli.close()
ser.close()
change(table)
interfaceTable()
print("Conexiones cerradas")