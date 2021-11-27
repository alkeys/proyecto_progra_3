import  tkinter as tk
from tkinter import ttk
import  matplotlib.pyplot as plt
import numpy as np
class Aplicacion:
    def __init__(self,master):
        self.master=master
        self.master.title("graficadora")
        self.master.geometry('350x350')

        self.inicializar()

    def inicializar(self):
        welcome=tk.Label(self.master,text='graficadora con matplotlib',font=("Helvetica",12))
        welcome.place(x=0 ,y=10)

        botonlineal=tk.Button(self.master,text="grafica de primer grado",bg="blue",fg="white")
        botonlineal["command"] = self.primer
        botonlineal.place(x=0,y=50)

        boton2 = tk.Button(self.master, text="grafica de segundo grado",bg="blue",fg="white")
        boton2.place(x=0,y=100)
        boton2["command"]=self.segu

        boton3 = tk.Button(self.master, text="grafica libre", bg="blue", fg="white")
        boton3.place(x=0, y=150)
        boton3["command"] = self.segu

    def primer(self):
       primerVenta=VentanaPrimerGrado(self.master)
       self.master.wait_window(primerVenta.ventanaSecundaria)

    def segu(self):
        pass;



class VentanaPrimerGrado:
    def __init__(self,master):
        self.master = master
        self.ventanaSecundaria=tk.Toplevel()
        self.ventanaSecundaria.title("grafica lineal")
        self.ventanaSecundaria.geometry('350x250')

        self.inicializar2()

    def inicializar2(self):
        welcome = tk.Label(self.ventanaSecundaria, text='ingrese los datos de la ecuacion y=x+c', font=("Helvetica", 12))
        welcome.place(x=0, y=10)

        welcome=tk.Label(self.ventanaSecundaria,text="ingrese x",font=("Helvetica", 12))
        welcome.place(x=0,y=50)
        self.tex_x=tk.Entry(self.ventanaSecundaria)
        self.tex_x.place(x=0,y=75)

        welcome = tk.Label(self.ventanaSecundaria, text="ingrese c", font=("Helvetica", 12))
        welcome.place(x=0, y=125)
        self.tex_c=tk.Entry(self.ventanaSecundaria)
        self.tex_c.place(x=0,y=150)

        enviar = tk.Button(self.ventanaSecundaria, text="graficar", bg="blue", fg="white")
        enviar.place(x=0, y=170)
        enviar["command"] = self.graficar

    def graficar(self):
        x=int(self.tex_x.get())
        c=int(self.tex_c.get())
        Vx=[]
        Vy=[]
        for i in range(-100,101):
            Vx.append((i))
            Vy.append((x*i)+c)
        plt.plot(Vx,Vy)
        plt.show()
        pass







def main():
    root=tk.Tk()
    ventana=Aplicacion(root)
    root.mainloop()


#/////////////////////////
main()