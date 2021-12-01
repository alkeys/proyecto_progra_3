from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import csv
import webbrowser

#Inicio del Main
def main():
    #Definiendo los eventos de los botones
    def primerg():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        bg3 = Label(app3, bg="#9fc5a0")
        bg3.place(relheight=1.0, relwidth=1.0)
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
            plt.subplots(constrained_layout=True)
            plt.plot(Vx,Vy)
            plt.ylabel("Datos en y")
            plt.xlabel("Datos en x")
            plt.title("Gráfica de Primer Grado")
            plt.show()

    def segundog():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        bg3 = Label(app3, bg="#9fc5a0")
        bg3.place(relheight=1.0, relwidth=1.0)
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
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            a=int(tex2_a.get())
            b=int(tex2_b.get())
            c=int(tex2_c.get())
            y=[]
            x=[]
            for i in range(-100,101):
                y.append((a*(pow(i,2)))+(i*b)+c)
                x.append(i)
            plt.plot(x,y, 'r')
            plt.ylabel("Datos en y")
            plt.xlabel("Datos en x")
            plt.title("Gráfica de Segundo Grado")
            plt.show()

    def cubic():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        bg3 = Label(app3, bg="#9fc5a0")
        bg3.place(relheight=1.0, relwidth=1.0)
        infoC = Label(app2, text=" ")
        infoC = Label(app2, text="Ingrese los datos de la ecuación\nf(x) = aX\u00B3+bX\u00B2+cX+d", font=("BarQ", 15), bg="#cec09d", fg="#282828")
        infoC.place(relx=0.5, relwidth=1.0, relheight=0.1, anchor="n")

        info_a = Label(app2, text="Ingrese a:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info_a.place(relx=0.1, y=100)
        tex3_a = Entry(app2)
        tex3_a.insert(0,"0")
        tex3_a.place(relx=0.1, y=125)

        info_b = Label(app2, text="Ingrese b:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info_b.place(relx=0.1, y=175)
        tex3_b = Entry(app2)
        tex3_b.insert(0, "0")
        tex3_b.place(relx=0.1, y=200)

        info_c = Label(app2, text="Ingrese c:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info_c.place(relx=0.1, y=250)
        tex3_c = Entry(app2)
        tex3_c.insert(0, "0")
        tex3_c.place(relx=0.1, y=275)

        info_d = Label(app2, text="Ingrese c:", font=("CaskaydiaCoveNerd", 12), bg="#cec09d", fg="#282828")
        info_d.place(relx=0.1, y=325)
        tex3_d = Entry(app2)
        tex3_d.insert(0, "0")
        tex3_d.place(relx=0.1, y=350)

        desc_enviar3 = Label(app3, text="Presione el botón para ver la gráfica", font=("BarQ", 15), bg="#9fc5a0", fg="black")
        desc_enviar3.place(relx=0.35, relwidth=0.8, height=50, anchor="n")
        enviar3 = Button(app3, text="Graficar", command=lambda:[graficarC()], font=("CaskaydiaCoveNerd", 12), bg="#9fc5a0", fg="#282828")
        enviar3.place(relx=-0.05, rely=0.1, relwidth=0.8, height=50)

        def graficarC():
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            a3=int(tex3_a.get())
            b3=int(tex3_b.get())
            c3=int(tex3_c.get())
            d3=int(tex3_d.get())
            y=[]
            x=[]
            for i in range(-50,51):
                x.append(i)
                y.append((a3*(pow(i,3)))+(b3*(pow(i,2)))+(i*c3)+d3)
            plt.plot(x,y, 'g')
            plt.title("Gráfica de Tercer Grado")
            plt.show()

    def libreg():
        bg = Label(app2, bg="#cec09d")
        bg.place(relheight=1.0, relwidth=1.0)
        bg3 = Label(app3, bg="#9fc5a0")
        bg3.place(relheight=1.0, relwidth=1.0)
        info3 = Label(app2, text=" ")
        info3 = Label(app2, text="Graficadora Libre (mediante archivo CSV)", font=("BarQ", 15), bg="#cec09d", fg="#282828")
        info3.place(relx=0.5, relwidth=1.0, relheight=0.1, anchor="n")

        #Abrir CSV
        file = askopenfilename()
        x = []
        y = []
        with open(file, encoding='utf-8') as csvF:
            plots = csv.reader(csvF, delimiter=',')
            next(plots)
            for row in plots:
                x.append(row[0])
                y.append(int(row[1]))

        #Mostrar datos
        def ObtenerData():
            x = []
            y = []
            with open(file, encoding='utf-8') as csvF:
                plots = csv.reader(csvF, delimiter=',')
                for row in plots:
                    x.append(row[0])
                    y.append(row[1])
            retorno=""
            retorno=""
            for i in range(len(x)):
                retorno+=x[i]+"   -   \t"+str(y[i])+"\n"
            return  retorno

        def graficarCircular():
            plt.figure(figsize=(8,5))
            cake = plt.pie(y, autopct='%1.2f%%')
            plt.legend(cake, labels=x, loc='best')
            plt.axis('equal')
            plt.tight_layout()
            plt.show()

        def graficarBarras():
            eje_x = (x)
            eje_y = (y)
            plt.subplots(constrained_layout=True)
            plt.bar(eje_x, eje_y, color="red")
            plt.xticks(rotation=90)
            plt.ylabel("Datos en y")
            plt.xlabel("Datos en x")
            plt.title("Gráfica de Barras")
            plt.show()

        def graficarBarrasHorizontal():
            eje_x = (x)
            eje_y = (y)
            plt.subplots(constrained_layout=True)
            plt.barh(eje_x, eje_y, color="green")
            plt.ylabel("Datos en y")
            plt.xlabel("Datos en x")
            plt.title("Gráfica de Barras Horizontales")
            plt.show()

        frame1=Frame(app2, bg="#cec09d")
        frame1.place(rely=0.1, relwidth=1.0, relheight=1.0)

        dato = ObtenerData()
        mostrar=Label(frame1, text="\nDatos del CSV\n\n"+f"{dato}", font=("Coolvetica 12"), bg="#cec09d", fg="black", justify=LEFT, borderwidth=2, relief="ridge")
        mostrar.place(relwidth=0.8, relx=0.1, rely=0.02)

        desc3 = Label(app3, text="Presione el botón para ver la gráfica", font=("BarQ", 15), bg="#9fc5a0", fg="black")
        desc3.place(relx=0.35, relwidth=0.8, height=50, anchor="n")

        pastel = Button(app3, text="Gráfica de pastel", command=lambda:[graficarCircular()], font=("CaskaydiaCoveNerd", 12), bg="#9fc5a0", fg="#282828")
        pastel.place(relx=-0.05, rely=0.1, relwidth=0.8, height=30)

        barras = Button(app3, text="Gráfica de barras", command=lambda:[graficarBarras()], font=("CaskaydiaCoveNerd", 12), bg="#9fc5a0", fg="#282828")
        barras.place(relx=-0.05, rely=0.16, relwidth=0.8, height=30)

        barrasH = Button(app3, text="Gráfica de barras horizontales", command=lambda:[graficarBarrasHorizontal()], font=("CaskaydiaCoveNerd", 12), bg="#9fc5a0", fg="#282828")
        barrasH.place(relx=-0.05, rely=0.22, relwidth=0.8, height=30)

    def acercaDe():
        bg_acerca_de = Label(app2, bg="#cec09d")
        bg_acerca_de.place(relheight=1.0, relwidth=1.0)
        desc_acerca = Label(app2, text="Acerca de la aplicación", font=("BarQ", 15), bg="#cec09d", fg="black")
        desc_acerca.place(relx=0.5, relwidth=1.0, relheight=0.1, anchor="n")
        info_acerca = Label(app2, text="GphicsCalc es una aplicación creada\npor 3 entrenadores Pokemon que su camino\nninja es graduarse de Ingeniería en Sistemas", font=("BarQ", 13), bg="#cec09d", fg="black")
        info_acerca.place(relx=0.5, rely=0.08, relwidth=1.0, relheight=0.15, anchor="n")
        devels_text = "Arana Aguirre, Inmer Vladimir   -   \tAA20047\nAviles Moran, Ernesto Alexander   -   \tAM18007\nTejada Cruz, Moisés Ernesto   -   \tTC20006"
        devels = Label(app2, text=devels_text, font=("BarQ", 13), bg="#cec09d", fg="black")
        devels.place(relx=0.5, rely=0.24, relwidth=1.0, relheight=0.15, anchor="n")

        url = "https://github.com/am18007ESD1352021/proyecto_progra_3"
        def OpenUrl():
            webbrowser.open_new(url)

        buttonUrl = Button(app2, text="Ir a GitHub", command=lambda:[OpenUrl()], font=("BarQ", 12), bg="#cec09d", fg="#282828", bd="1")
        buttonUrl.place(relx=0.5, rely=0.40, relwidth=0.8, height=50, anchor="n")

    #Inicio de la GUI del programa
    root = Tk()

    HEIGHT=600
    WIDTH=1000

    root.title("GphicsCalc")
    root.resizable(0,0)
    ico = Image.open("img/logo.png")
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
    logo = Image.open("img/logo.png")
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

    boton3 = Button(app, text="Gráfica de Tercer Grado", command=lambda:[cubic()], font=("BarQ"), bg="#ebdbb2", fg="#282828", bd="1")
    boton3.place(relx=0.35, rely=0.27, relwidth=0.8, height=50)

    botonFinal = Button(app, text="Gráfica Libre (mediante CSV)", command=lambda:[libreg()], font=("BarQ"), bg="#ebdbb2", fg="#282828", bd="1")
    botonFinal.place(relx=0.35, rely=0.36, relwidth=0.8, height=50)

    acerca = Button(app, text="Acerca de", command=lambda:[(acercaDe())], font=("BarQ"), bg="#ebdbb2", fg="#282828", bd="1")
    acerca.place(relx=0.35, rely=0.45, relwidth=0.8, height=50)

    #---------Fin del mainloop---------#
    root.mainloop()

main()
#Fin del Main
