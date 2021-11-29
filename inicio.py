import  tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
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

        boton3 = tk.Button(self.master, text="graficar CSV", bg="blue", fg="white")
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
    def __init__(self, master=None):
        self.master = master
        self.VentaLibre = tk.Toplevel()
        self.VentaLibre.title("graficadora Libre")
        self.VentaLibre.geometry('600x400')
        self.iniciar()

    def iniciar(self):
        self.file = askopenfilename()
        self.x = []
        self.y = []
        with open(self.file, encoding='utf-8') as csvF:
            plots = csv.reader(csvF, delimiter=',')
            next(plots)
            for row in plots:
                self.x.append(row[0])
                self.y.append(int(row[1]))
        dato= self.OctenerData()
        mostar=tk.Label(self.VentaLibre, text=f"{dato}", bg="blue", fg="white")
        mostar.place(x=10,y=0)

        boton1 = tk.Button(self.VentaLibre, text="graficar circular", bg="blue", fg="white")
        boton1.place(x=0, y=250)
        boton1["command"] = self.graficarCircular

        boton2 = tk.Button(self.VentaLibre, text="graficar de Barras", bg="blue", fg="white")
        boton2.place(x=125, y=250)
        boton2["command"] = self.graficarBarras

        boton3 = tk.Button(self.VentaLibre, text="graficar de Barra Horizontal", bg="blue", fg="white")
        boton3.place(x=275, y=250)
        boton3["command"] = self.graficarBarrasHorizontal

        boton4 = tk.Button(self.VentaLibre, text="graficar de Areas", bg="blue", fg="white")
        boton4.place(x=475, y=250)
        boton4["command"] = self.graficarAreas

        boton5 = tk.Button(self.VentaLibre, text="graficar de Histograma", bg="blue", fg="white")
        boton5.place(x=0, y=300)
        boton5["command"] = self.graficarHistograma

        boton6 = tk.Button(self.VentaLibre, text="graficar de Sectores", bg="blue", fg="white")
        boton6.place(x=175, y=300)
        boton6["command"] = self.graficarSectores

        boton7 = tk.Button(self.VentaLibre, text="graficar de Violín", bg="blue", fg="white")
        boton7.place(x=300, y=300)
        boton7["command"] = self.graficarViolin


#se definio este metodo para mostra los datos
    def OctenerData(self):
        x = []
        y = []
        with open(self.file, encoding='utf-8') as csvF:
            plots = csv.reader(csvF, delimiter=',')
            for row in plots:
                x.append(row[0])
                y.append(row[1])
        retorno=""
        for i in range(len(self.x)):
            retorno+=x[i]+"  "+str(y[i])+"\n"
        return  retorno

#programacion de botones
    def graficarCircular(self):
        plt.pie(self.y, labels=self.x)
        plt.show()
    def graficarBarras(self):

        pass

    def graficarBarrasHorizontal(self):

        pass

    def graficarAreas(self):

        pass
    #talvez no funcionen
###############################################################
    def graficarHistograma(self):
        pass

    def graficarSectores(self):

        pass

    def graficarViolin(self):

        pass
###############################################################




def main():
    root=tk.Tk()
    ventana=Aplicacion(root)
    root.mainloop()

#/////////////////////////
main()