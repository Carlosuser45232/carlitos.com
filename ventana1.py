import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
import time
import sys
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

class FormularioArticulos:

    def __init__(self):
        self.ventana0=tk.Tk()
        self.ventana0.title("LOGIN")
        self.ventana0.geometry("1000x700")
        self.ventana0.resizable(0,0)

        self.imagen=tk.PhotoImage(file="fondo bolognesi.gif")

        self.fondoimagen=tk.Label(self.ventana0,image=self.imagen).place(x=0,y=0)

        self.label1=ttk.Label(self.ventana0,text="Colegio",foreground="White",background="Black",font=("Arial",30)).place(x=450,y=50)
        
        self.label2=ttk.Label(self.ventana0,text="Francisco Bolognesi",foreground="White",background="Black",font=("Arial",30)).place(x=350,y=100)


        self.label3=ttk.Label(self.ventana0,text="Colegio",foreground="White",background="Black",font=("Arial",30))
        self.label3.grid(column=0,row=1)

        self.label4=ttk.Label(self.ventana0,text="Usuario",foreground="White",background="Black",font=("Arial",30)).place(x=350,y=200)

        #Entrys, label and button 

        self.usuario=tk.StringVar()

        self.entry1=ttk.Entry(self.ventana0,textvariable=self.usuario,width=30).place(x=350,y=270)

        self.label4=ttk.Label(self.ventana0,text="Contraseña",foreground="White",background="Black",font=("Arial",30)).place(x=350,y=330)

        self.contraseña=tk.StringVar()

        self.entry2=ttk.Entry(self.ventana0,textvariable=self.contraseña,width=30,show="*").place(x=350,y=400)
         
        self.boton1=ttk.Button(self.ventana0,text="Ingresar",command=self.ingresar).place(x=370,y=450)

        self.boton2=ttk.Button(self.ventana0,text="Salir",command=self.salir).place(x=450,y=450)
        self.hora()

        self.ventana0.mainloop()

    def hora(self):

        hora=time.strftime("%H:%M:%S")

        self.label3.configure(text=hora)
        self.ventana0.after(1000,self.hora)
    
    def ingresar(self):
        user=["carlitos30"]
        contra=["carlitos30"]
        if str(self.usuario.get()) in user and str(self.contraseña.get()):
            self.ventana0.destroy() 
            self.ventana1()
        else:
            mb.showerror("Contraseña Erronea ","Usuario o contraseña erronea, porfavor Pruebe de nuevo")
    
    def salir(self):
       pass
    def ventana1(self):
        pass


Ventana1=FormularioArticulos()