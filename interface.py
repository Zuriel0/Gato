#importacion de librerias para gato
from tkinter import *
from tkinter import messagebox

#Funciones
def disable():
    for i in range(0,9):
        button_list[i].config(state="disable")
        
def start():
    for i in range(0,9):
        button_list[i].config(bg="lightgray")
        target[i] = "V"
    global namePlayer_1,namePlayer_2
    namePlayer_1 = "cliente"
    namePlayer_2 = "servidor"
    playerTrun.set("Turno: " + namePlayer_1)
    return "1"
def change(table):
    for i in range(0,9):
        button_list[i].config(text=table[i])
        

# Configuraciones de ventana 

window  = Tk()
window.geometry("400x400")
window.title("Gato")

#condiciones iniciales del juego
turno = 0
namePlayer_1 = "X"
namePlayer_2 = "O"

#interfase del juego
button_list = []
target = [] # X, O o Void (V)
playerTrun = StringVar()

for i in range(0,9):
    target.append("V")
#primera columna    
cell_0 = Button(window, width=9, height=3)
button_list.append(cell_0)
cell_0.place(x=60,y=50)
cell_1 = Button(window, width=9, height=3)
button_list.append(cell_1)
cell_1.place(x=160,y=50)
cell_3 = Button(window, width=9, height=3)
button_list.append(cell_3)
cell_3.place(x=260,y=50)
#segunda columna 
cell_4 = Button(window, width=9, height=3)
button_list.append(cell_4)
cell_4.place(x=60,y=150)
cell_5 = Button(window, width=9, height=3)
button_list.append(cell_5)
cell_5.place(x=160,y=150)
cell_6 = Button(window, width=9, height=3)
button_list.append(cell_6)
cell_6.place(x=260,y=150)
#tercera columan 
cell_7 = Button(window, width=9, height=3)
button_list.append(cell_7)
cell_7.place(x=60,y=250)
cell_8 = Button(window, width=9, height=3)
button_list.append(cell_8)
cell_8.place(x=160,y=250)
cell_9 = Button(window, width=9, height=3)
button_list.append(cell_9)
cell_9.place(x=260,y=250)
#boton de inicio
playerTrunE = Label(window, textvariable=playerTrun).place(x=120, y=20)
start = Button(window,bg="#060",fg="black",text="Inciar Juego",width=15,height=3, command=start).place(x=140, y= 325)
disable()
#tablero
def interfaceTable():
    window.mainloop()
