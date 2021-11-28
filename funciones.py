#Ignora este archivo, solo fueron unas funciones de prueba que hice
from tkinter import *
from PIL import Image, ImageTk

#place an image on the grid
def display_logo(url, row, column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/5),int(img.size[1]/5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="black")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)
