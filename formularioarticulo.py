
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import psycopg2
import articulos
import time
import sys
class FormularioArticulos:

    def __init__(self):
        self.ventana0=tk.Tk()
        self.ventana0.title("LOGIN")
        self.ventana0.geometry("1000x700")
        #self.ventana0.resizable(0,0)

        self.imagen=tk.PhotoImage(file="fondo colegio.gif")

        self.fondoimagen=tk.Label(self.ventana0,image=self.imagen).place(x=0,y=0)

        self.label1=ttk.Label(self.ventana0,text="Colegio",foreground="White",background="Black",font=("Arial",30)).place(x=450,y=50)
        
        self.label2=ttk.Label(self.ventana0,text="Miguel Grau",foreground="White",background="Black",font=("Arial",30)).place(x=350,y=100)


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
        sys.exit(0)

    """--------------------------------------------------------------------------------------------------------------"""
    def ventana1(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Colegio Miguel Grau")
        self.ventana1.geometry("1000x700")
        #afasfhgadskkkkkkkkkkkkkkkkk
        #self.ventana1.configure(bg="Blue")
        self.imagen=tk.PhotoImage(file="imagen3.gif")

        self.fondoimagen=tk.Label(self.ventana1,image=self.imagen).place(x=700,y=350)

        self.imagen=tk.PhotoImage(file="imagen3.gif")

        self.fondoimagen=tk.Label(self.ventana1,image=self.imagen).place(x=700,y=350)

        self.imagen2=tk.PhotoImage(file="imagen1.gif")

        self.fondoimagen2=tk.Label(self.ventana1,image=self.imagen2).place(x=650,y=50)

        self.imagen3=tk.PhotoImage(file="imagen2.gif")

        self.fondoimagen3=tk.Label(self.ventana1,image=self.imagen3).place(x=50,y=350)


        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de Alumno")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Alumno")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text=" matricula ID    :")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Subir", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "El alumno fue cargado")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por ID")
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Alumnos")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Matricula ID:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe dicho alumno")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="Alumnos")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+
                                              "\nnombre:"+fila[1]+
                                              "\nMatricula ID:"+str(fila[2])+"\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de Alumnos")
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="Alumnos")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el alumno con dicho código")
        else:
            mb.showinfo("Información", "No existe un alumno con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar Alumno")
        self.labelframe1=ttk.LabelFrame(self.pagina5, text="Alumno")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Matricula ID:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el Alumno")
        else:
            mb.showinfo("Información", "No existe un Alumno con dicho código")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un Alumno con dicho código")


aplicacion1=FormularioArticulos()
#aplicacion1.ventana1()
