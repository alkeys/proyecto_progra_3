import  tkinter as tk
from tkinter import ttk
import  matplotlib.pyplot as plt
import numpy as np
import csv


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
        boton3["command"] = self.libre

    def primer(self):
       primerVenta=VentanaPrimerGrado(self.master)
       self.master.wait_window(primerVenta.ventanaSecundaria)

    def segu(self):
        segunVentana=VentanaSegundoGrado(self.master)
        self.master.wait_window(segunVentana.ventanaSecundaria)

    def libre(self):
        VentanaLibree = VentanaLibre(self.master)
        self.master.wait_window(VentanaLibree.VentaLibre)
        pass

class VentanaPrimerGrado:
    def __init__(self,master):
        self.master = master
        self.ventanaSecundaria=tk.Toplevel()
        self.ventanaSecundaria.title("grafica lineal")
        self.ventanaSecundaria.geometry('350x250')
        self.inicializar2()

    def inicializar2(self):
        welcome = tk.Label(self.ventanaSecundaria, text='ingrese los datos de la ecuacion y=ax+c', font=("Helvetica", 12))
        welcome.place(x=0, y=10)

        welcome=tk.Label(self.ventanaSecundaria,text="ingrese a",font=("Helvetica", 12))
        welcome.place(x=0,y=50)
        self.tex_x=tk.Entry(self.ventanaSecundaria)
        self.tex_x.insert(0, "0")
        self.tex_x.place(x=0,y=75)

        welcome = tk.Label(self.ventanaSecundaria, text="ingrese c", font=("Helvetica", 12))
        welcome.place(x=0, y=125)
        self.tex_c=tk.Entry(self.ventanaSecundaria)
        self.tex_c.insert(0, "0")
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

class VentanaSegundoGrado:
    def __init__(self,master):
        self.master = master
        self.ventanaSecundaria=tk.Toplevel()
        self.ventanaSecundaria.title("grafica de segundo grado")
        self.ventanaSecundaria.geometry('350x250')
        self.iniciar()

    def iniciar(self):
        texto=tk.Label(self.ventanaSecundaria,text="ingrese aX^2+bX+c",font=("Helvetica", 12))
        texto.place(x=0,y=10)

        texto = tk.Label(self.ventanaSecundaria, text="ingrese a", font=("Helvetica", 12))
        texto.place(x=0, y=50)
        self.tex_a = tk.Entry(self.ventanaSecundaria)
        self.tex_a.insert(0,"0")
        self.tex_a.place(x=0, y=75)

        texto = tk.Label(self.ventanaSecundaria, text="ingrese b", font=("Helvetica", 12))
        texto.place(x=0, y=100)
        self.tex_b = tk.Entry(self.ventanaSecundaria)
        self.tex_b.insert(0, "0")
        self.tex_b.place(x=0, y=130)

        texto = tk.Label(self.ventanaSecundaria, text="ingrese c", font=("Helvetica", 12))
        texto.place(x=0, y=150)
        self.tex_c = tk.Entry(self.ventanaSecundaria)
        self.tex_c.insert(0, "0")
        self.tex_c.place(x=0, y=170)

        enviar = tk.Button(self.ventanaSecundaria, text="graficar", bg="blue", fg="white")
        enviar.place(x=0, y=200)
        enviar["command"] = self.graficar

    def graficar(self):
        a=int(self.tex_a.get())
        b=int(self.tex_b.get())
        c=int(self.tex_c.get())
        y=[]
        x=[]
        for i in range(-100,101):
            y.append((a*(pow(i,2)))+(i*b)+c)
            x.append(i)
        plt.plot(x,y)
        plt.show()

class VentanaLibre():
    def __init__(self, master):
        self.master = master
        self.VentaLibre = tk.Toplevel()
        self.VentaLibre.title("graficadora Libre")
        self.VentaLibre.geometry('350x350')
        self.iniciar()

    def iniciar(self):
        self.x = []
        self.y = []
        with open('datos.csv', encoding='utf-8') as csvF:
            plots = csv.reader(csvF, delimiter=',')
            next(plots)
            for row in plots:
                self.x.append(row[0])
                self.y.append(int(row[1]))

        enviar = tk.Button(self.VentaLibre, text="graficar", bg="blue", fg="white")
        enviar.place(x=0, y=250)
        enviar["command"] = self.graficar

    def graficar(self):
        plt.pie(self.y, labels=self.x)
        plt.show()
        pass

def main():
    root=tk.Tk()
    ventana=Aplicacion(root)
    root.mainloop()

#/////////////////////////
main()