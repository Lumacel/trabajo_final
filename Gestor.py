from tkinter import *
from tkinter import ttk

class Ventana:
	def __init__(self):

		self.root = Tk()
		self.root.title("GESTOR") 
		self.root.geometry("1000x500+300+300")
		self.root.resizable(0,0)

		self.afiliados = []
		self.obras_sociales=["IOMA","OSPE"]

		self.btn_abrir_ventana= Button(self.root,text="ACEPTAR",command= self.abrir_ventana)
		self.btn_abrir_ventana.place(x=10,y=400)

		self.afiliados = crear_lista_afiliados()
		print(self.afiliados)
		self.cant_afil= len(self.afiliados)
		print(self.cant_afil)
	

		self.ver_tabla()

	def ver_tabla(self,filas=10):
		self.tabla = ttk.Treeview(self.root, height=filas,columns=("APELLIDO","NOMBRE","Nº DOCUMENTO","Nº AFILIADO","Nº TELEFONO","OBRA SOCIAL"))
		self.tabla.pack(expand=False)
		
		## --- barra scroll
		self.scroll = Scrollbar(self.root, orient="vertical", command=self.tabla.yview)
		self.scroll.place(x=980, y=10, height=200)
		self.tabla.configure(yscrollcommand=self.scroll.set)

		## --- formato a las columnas
		self.tabla.column("#0", width=0, stretch=NO )
		self.tabla.column("APELLIDO", anchor=W, width=250)
		self.tabla.column("NOMBRE", anchor=W, width=250)
		self.tabla.column("Nº DOCUMENTO", anchor=CENTER, width=120)
		self.tabla.column("Nº AFILIADO", anchor=CENTER, width=120)
		self.tabla.column("Nº TELEFONO", anchor=CENTER, width=120)
		self.tabla.column("OBRA SOCIAL", anchor=CENTER, width=120)
		## --- indicar cabecera
		self.tabla.heading("#0", text="", anchor=W)
		self.tabla.heading("#1", text="APELLIDO", anchor=CENTER)
		self.tabla.heading("#2", text="NOMBRE", anchor=CENTER)
		self.tabla.heading("#3", text="Nº DOCUMENTO", anchor=CENTER)
		self.tabla.heading("#4", text="Nº AFILIADO", anchor=CENTER)
		self.tabla.heading("#5", text="Nº TELEFONO", anchor=CENTER)
		self.tabla.heading("#6", text="OBRA SOCIAL", anchor=CENTER)

	def abrir_ventana(self):

		self.top_level = Toplevel()
		self.top_level.resizable(0,0)
		self.top_level.title("DATOS AFILIADO")
		self.top_level.geometry("370x250")

		self.apellido = StringVar()
		self.nombre = StringVar() 
		self.dni = StringVar()
		self.afiliado = StringVar()
		self.telefono = StringVar()
		
		self.lbl_apellido = Label(self.top_level, text = "APELLIDO", width=20, relief="groove")
		self.lbl_apellido.place(x=10,y=10)
		self.entry_apellido = Entry(self.top_level,textvariable = self.apellido,width=30)
		self.entry_apellido.place(x=170,y=10)

		self.lbl_nombre = Label(self.top_level, text = "NOMBRE", width=20, relief="groove")
		self.lbl_nombre.place(x=10,y=40)
		self.entry_nombre = Entry(self.top_level,textvariable = self.nombre,width=30)
		self.entry_nombre.place(x=170,y=40) 

		self.lbl_dni = Label(self.top_level, text = "Nº DOCUMENTO", width=20, relief="groove")
		self.lbl_dni.place(x=10,y=70)
		self.entry_dni = Entry(self.top_level,textvariable = self.dni,width=30)
		self.entry_dni.place(x=170,y=70)

		self.lbl_afiliado = Label(self.top_level, text = "Nº AFILIADO", width=20, relief="groove")
		self.lbl_afiliado.place(x=10,y=100)
		self.entry_afiliado = Entry(self.top_level,textvariable = self.afiliado,width=30)
		self.entry_afiliado.place(x=170,y=100)

		self.lbl_telefono = Label(self.top_level, text = "Nº TELEFONO", width=20, relief="groove")
		self.lbl_telefono.place(x=10,y=130)
		self.entry_telefono = Entry(self.top_level,textvariable = self.telefono,width=30)
		self.entry_telefono.place(x=170,y=130)

		self.lbl_obrasocial = Label(self.top_level, text = "OBRA SOCIAL", width=20, relief="groove")
		self.lbl_obrasocial.place(x=10,y=160)
		self.entry_obrasocial = ttk.Combobox(self.top_level,values=self.obras_sociales,state="readonly",width=10)
		self.entry_obrasocial.place(x=170,y=160)

		self.btn_ingresar= Button(self.top_level,text="GRABAR DATOS",command= self.agregar_afiliado,width=15)
		self.btn_ingresar.place(x=10,y=215)
		self.btn_salir= Button(self.top_level,text="SALIR",command= self.salir_top_level,width=15)
		self.btn_salir.place(x=245,y=215)
		
		self.entry_apellido.focus()

	def salir_top_level(self):
		self.top_level.destroy()

	def get_apellido(self):
		return self.apellido.get()

	def agregar_afiliado(self):
		self.afiliados.append(self.get_apellido().upper())
		print(self.afiliados)
		print(self.entry_obrasocial.get())

def crear_lista_afiliados(archivo="afiliados.txt",obra_social="TODO"): 
    lista=[]
    try:
	    with open(archivo, 'r', encoding='latin1') as datos:
	        items = datos.readline().upper().rstrip().split(',')
	        for linea in datos:
	            linea = linea.upper().rstrip().split(',')
	            if obra_social != 'TODO':
	                if linea[-1] != obra_social: continue # filtra si no pertenece a obra social pasada por parametro
	                lista.append(dict(zip(items,linea)))
	            else:
	                lista.append(dict(zip(items,linea)))
	        return lista

    except Exception as e:
    	print(f"Error!! {e}")
	


def app():
	v = Ventana()
	v.root.mainloop()
	
if __name__ == "__main__":
	app()