import  tkinter as tk
from tkinter import ttk
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

        pass;

    def segu(self):
        pass;





def main():
    root=tk.Tk()
    ventana=Aplicacion(root)
    root.mainloop()


#/////////////////////////
main()