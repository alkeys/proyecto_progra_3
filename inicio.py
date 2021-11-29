from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np

def main():
    #Definiendo los eventos de los botones
    def primerg():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        info1 = Label(app2, text="Ingrese los datos de la ecuación y = ax + c\n", font=("BarQ", 15), bg="#cec09d", fg="black")
        info1.place(relx=0.5, relwidth=1.0, relheight=0.1, anchor="n")

        info1_a = Label(app2,text="Ingrese a:",font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info1_a.place(relx=0.1,y=50)
        tex_x1 = Entry(app2)
        tex_x1.insert(0, "0")
        tex_x1.place(relx=0.1,y=75)

        info1_c = Label(app2, text="Ingrese c:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info1_c.place(relx=0.1, y=125)
        tex_c1 = Entry(app2)
        tex_c1.insert(0, "0")
        tex_c1.place(relx=0.1,y=150)

        desc_enviar1 = Label(app3, text="Presione el botón para ver la gráfica", font=("BarQ", 15), bg="#9fc5a0", fg="black")
        desc_enviar1.place(relx=0.35, relwidth=0.8, height=50, anchor="n")
        enviar1 = Button(app3, text="Graficar", command=lambda:[graficar1()], font=("CaskaydiaCoveNerd", 12), bg="#9fc5a0", fg="#282828")
        enviar1.place(relx=-0.05, rely=0.1, relwidth=0.8, height=50)

        def graficar1():
            x=int(tex_x1.get())
            c=int(tex_c1.get())
            Vx=[]
            Vy=[]
            for i in range(-100,101):
                Vx.append((i))
                Vy.append((x*i)+c)
            plt.plot(Vx,Vy)
            plt.show()

    def segundog():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        info2 = Label(app2, text=" ")
        text2_i = "Ingrese los datos de la ecuación aX\u00B2+bX+c\n"
        info2 = Label(app2, text=text2_i, font=("BarQ", 15), bg="#cec09d", fg="#282828")
        info2.place(relx=0.5, relwidth=1.0, relheight=0.1, anchor="n")

        info2_a = Label(app2, text="Ingrese a:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info2_a.place(relx=0.1, y=50)
        tex2_a = Entry(app2)
        tex2_a.insert(0,"0")
        tex2_a.place(relx=0.1, y=75)

        info2_b = Label(app2, text="Ingrese b:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info2_b.place(relx=0.1, y=125)
        tex2_b = Entry(app2)
        tex2_b.insert(0, "0")
        tex2_b.place(relx=0.1, y=150)

        info2_c = Label(app2, text="Ingrese c:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info2_c.place(relx=0.1, y=200)
        tex2_c = Entry(app2)
        tex2_c.insert(0, "0")
        tex2_c.place(relx=0.1, y=225)

        desc_enviar2 = Label(app3, text="Presione el botón para ver la gráfica", font=("BarQ", 15), bg="#9fc5a0", fg="black")
        desc_enviar2.place(relx=0.35, relwidth=0.8, height=50, anchor="n")
        enviar2 = Button(app3, text="Graficar", command=lambda:[graficar2()], font=("CaskaydiaCoveNerd", 12), bg="#9fc5a0", fg="#282828")
        enviar2.place(relx=-0.05, rely=0.1, relwidth=0.8, height=50)

        def graficar2():
            a=int(tex2_a.get())
            b=int(tex2_b.get())
            c=int(tex2_c.get())
            y=[]
            x=[]
            for i in range(-100,101):
                y.append((a*(pow(i,2)))+(i*b)+c)
                x.append(i)
            plt.plot(x,y)
            plt.show()

    def libreg():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        info3 = Label(app2, text=" ")
        info3 = Label(app2, text="Inmer se la come\ndoblada", font=("BarQ", 25), bg="#cec09d", fg="#282828")
        info3.place(relx=0.5, relwidth=1.0, relheight=0.1, anchor="n")
    #Inicio de la GUI del programa
    root = Tk()

    HEIGHT=600
    WIDTH=1000

    root.title("GphicsCalc")
    ico = Image.open("logo.png")
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    C = Canvas(root, height=HEIGHT, width=WIDTH)
    C.pack(fill=X)

    #Espacio para la cabecera
    cabecera = Frame(root, bg="#282828")
    cabecera.place(relx=0.5, y=0.1, relwidth=1.0, relheight=0.2, anchor="n")
    nombre = Label(cabecera, text="GphicsCalc", font=("ChocolateCookies", 30), bg="#282828", fg="white")
    nombre.place(relx=0.78, rely=0.2)
    desc = Label(cabecera, text="Graficadora con Matplotlib", font=("BarQ", 15), bg="#282828", fg="white")
    desc.place(relx=0.77, rely=0.6)

    #Logo
    logo = Image.open("logo.png")
    #logo = ImageTk.PhotoImage(file="logo.png")
    resized = logo.resize((int(logo.size[0]/5),int(logo.size[1]/5)), Image.ANTIALIAS)
    new_logo = ImageTk.PhotoImage(resized)
    my_logo = Label(cabecera, image=new_logo, bg="#282828")
    my_logo.pack(side=LEFT)

    #Espacio de la App
    app = Frame(root, width=1000, height=600, bg="#ebdbb2")
    app.place(relx=0.0, rely=0.2, relwidth=0.5, relheight=1.0, anchor="n")
    descApp = Label(app, text="Seleccione una opción", font=("BarQ", 15), bg="#ebdbb2", fg="black")
    descApp.place(relx=0.35, rely=0.01, relwidth=0.8, height=50)

    app2 = Frame(root, width=1000, height=600, bg="#cec09d")
    app2.place(relx=0.45, rely=0.2, relwidth=0.42, relheight=1.0, anchor="n")

    app3 = Frame(root, width=1000, height=600, bg="#9fc5a0")
    app3.place(relx=0.90, rely=0.2, relwidth=0.5, relheight=1.0, anchor="n")

    #Botones
    boton1 = Button(app, text="Gráfica de Primer Grado", command=lambda:[primerg()], font=("BarQ"), bg="#ebdbb2", fg="#282828", bd="1")
    boton1.place(relx=0.35, rely=0.09, relwidth=0.8, height=50)

    boton2 = Button(app, text="Gráfica de Segundo Grado", command=lambda:[segundog()], font=("BarQ"), bg="#ebdbb2", fg="#282828", bd="1")
    boton2.place(relx=0.35, rely=0.18, relwidth=0.8, height=50)

    boton3 = Button(app, text="Gráfica Libre", command=lambda:[libreg()], font=("BarQ"), bg="#ebdbb2", fg="#282828", bd="1")
    boton3.place(relx=0.35, rely=0.27, relwidth=0.8, height=50)

    #Espacio de la App 1
    #---------Fin del mainloop---------#
    root.mainloop()

main()
