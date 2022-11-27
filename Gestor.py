from tkinter import *
from tkinter import ttk

class App:

	OBRAS_SOCIALES = ["IOMA", "OSPE"]
	VISTA_OBRASOCIAL = ["TODO", "IOMA", "OSPE"]


	def __init__(self):
		self.afiliados = []
		self.afil_target = []
		self.current_obrasocial=""

		self.root = Tk()  
		self.root.title("GESTOR") 
		self.root.geometry("900x420+300+300")
		self.root.resizable(0,0)

		# -- agrega estilo 
		self.style = ttk.Style()
		self.style.theme_use('winnative') 

		# -- label para información
		self.text_info = StringVar()
		self.lbl_info = Label(self.root, textvariable = self.text_info , width=114, relief="ridge",bg="#c7e5f7",fg="blue", bd=4)
		self.lbl_info.place(x=47,y=240)
		
		# -- Nueva ventana dentro de la raiz(root)
		self.frame1 = Frame(self.root,bg="lightgrey",relief="ridge",bd=4)
		self.frame1.place(x=48,y=282)
		self.frame1.configure(width=808,height=121)

		self.separador= ttk.Separator(self.frame1, orient="vertical")
		self.separador.place(relx=0.33, rely=0, relwidth=0.005, relheight=1) 

		self.separador= ttk.Separator(self.frame1, orient="vertical")
		self.separador.place(relx=0.66, rely=0, relwidth=0.005, relheight=1)


		self.btn_agregar= Button(self.frame1,text="AGREGAR", width=29, bd=3, command= self.abrir_ventana_entry)
		self.btn_agregar.place(x=26,y=10) 


		self.btn_editar= Button(self.frame1,text="EDITAR", width=29, bd=3, command= self.editar_afiliado)
		self.btn_editar.place(x=26,y=45)


		self.btn_eliminar= Button(self.frame1,text="ELIMINAR", width=29, bd=3, command= self.eliminar_afiliado)
		self.btn_eliminar.place(x=26,y=80)


		self.lbl_obra_social= Label(self.frame1,text="OBRA SOCIAL", relief= "ridge",width=14, bg="lightgrey", fg="black")
		self.lbl_obra_social.place(x=294,y=10)

		self.entry_obra_social = ttk.Combobox(self.frame1,values=App.VISTA_OBRASOCIAL,state="readonly",width=12)
		self.entry_obra_social.place(x=407,y=10)

		self.btn_actualizar= Button(self.frame1,text="ACTUALIZAR VISTA",width=29, bd=3, command= self.actualizar)
		self.btn_actualizar.place(x=296,y=45)

		

		##############  estas funciones estaran asignadas a botones #########
		self.crear_lista_afiliados() 
		self.ordenar_lista_afiliados()
		self.crear_tabla(10)  
		self.cargar_tabla(self.get_afiliados_sort(),self.get_obrasocial())
		##################################################################################

	def crear_tabla(self,filas=10):
		self.tabla = ttk.Treeview(self.root, height=filas,columns=("APELLIDO","NOMBRE","DNI/AFILIADO","TELEFONO","OBRA SOCIAL"))
		self.tabla.pack(expand=False)
		
		# --- agrega color al heading
		self.style.configure('Treeview.Heading', background="#c7e5f7")
	
		# --- barra scroll
		self.scroll = Scrollbar(self.root, orient="vertical", command=self.tabla.yview)
		self.scroll.place(x=860, y=10, height=210)
		self.tabla.configure(yscrollcommand=self.scroll.set)

		# --- formato a las columnas
		self.tabla.column("#0", width=0, stretch=NO )
		self.tabla.column("APELLIDO", anchor=W, width=200)
		self.tabla.column("NOMBRE", anchor=W, width=200)
		self.tabla.column("DNI/AFILIADO", anchor=E, width=150)
		self.tabla.column("TELEFONO", anchor=E, width=150)
		self.tabla.column("OBRA SOCIAL", anchor=CENTER, width=100)

		# --- indicar cabecera
		self.tabla.heading("#0", text="", anchor=CENTER)
		self.tabla.heading("#1", text="APELLIDO", anchor=CENTER)
		self.tabla.heading("#2", text="NOMBRE", anchor=CENTER)
		self.tabla.heading("#3", text="DNI/AFILIADO", anchor=CENTER)
		self.tabla.heading("#4", text="TELEFONO", anchor=CENTER)
		self.tabla.heading("#5", text="OBRA SOCIAL", anchor=CENTER)

	def abrir_ventana_entry(self):
		
		self.top_level = Toplevel()
		self.top_level.resizable(0,0)
		self.top_level.title("DATOS AFILIADO")
		self.top_level.geometry("370x250")

		self.apellido = StringVar()
		self.nombre = StringVar() 
		self.dni = StringVar()
		self.afiliado = StringVar()
		self.telefono = StringVar()
		
		self.lbl_apellido = Label(self.top_level, text = "APELLIDO", width=20, relief="ridge")
		self.lbl_apellido.place(x=10,y=10)
		self.entry_apellido = Entry(self.top_level,textvariable = self.apellido,width=30)
		self.entry_apellido.place(x=170,y=10)

		self.lbl_nombre = Label(self.top_level, text = "NOMBRE", width=20, relief="ridge")
		self.lbl_nombre.place(x=10,y=40)
		self.entry_nombre = Entry(self.top_level,textvariable = self.nombre,width=30)
		self.entry_nombre.place(x=170,y=40) 

		self.lbl_dni_afiliado = Label(self.top_level, text = "DNI/AFILIADO", width=20, relief="ridge")
		self.lbl_dni_afiliado.place(x=10,y=70)
		self.lbl_dni_afiliado= Entry(self.top_level,textvariable = self.dni,width=30)
		self.lbl_dni_afiliado.place(x=170,y=70)

		self.lbl_telefono = Label(self.top_level, text = "TELEFONO", width=20, relief="ridge")
		self.lbl_telefono.place(x=10,y=100)
		self.entry_telefono = Entry(self.top_level,textvariable = self.afiliado,width=30)
		self.entry_telefono.place(x=170,y=100)

		self.lbl_obra_social = Label(self.top_level, text = "OBRA SOCIAL", width=20, relief="ridge",)
		self.lbl_obra_social.place(x=10,y=130)
		self.entry_o_s_toplevel = ttk.Combobox(self.top_level,values=App.OBRAS_SOCIALES,state="readonly",width=6)
		self.entry_o_s_toplevel.place(x=170,y=130)

		self.btn_ingresar= Button(self.top_level,text="GRABAR DATOS",bd=3, width=15, command= self.agregar_afiliado)
		self.btn_ingresar.place(x=10,y=215)
		self.btn_salir= Button(self.top_level,text="SALIR", bd=3, width=15, command= self.salir_top_level)
		self.btn_salir.place(x=245,y=215)
		
		self.entry_apellido.focus()
		self.deshabilitar_botones_App()

	def crear_lista_afiliados(self,archivo="afiliados.txt"): 
		try:
			with open(archivo, 'r', encoding='latin1') as datos:
				items = datos.readline().upper().rstrip().split(',')
				for linea in datos:
					linea = linea.upper().rstrip().split(',')					
					self.afiliados.append(linea)	
				self.items = items
		except Exception as e:
			self.text_info.set(f"Error!! {e}")

	def cargar_tabla(self,lista,obrasocial=""): # --- agrega datos
		for afiliado in lista: 
			if obrasocial != "":
				if afiliado[-1] != obrasocial: continue # filtra si no pertenece a obra social pasada por parametro
				self.tabla.insert("", END, text="", values=(afiliado[0],afiliado[1], afiliado[2], afiliado[3],afiliado[4]))
			else:
				self.tabla.insert("", END, text="", values=(afiliado[0],afiliado[1], afiliado[2], afiliado[3],afiliado[4]))

	def deshabilitar_botones_App(self):
		self.btn_agregar.config(state="disabled")
		self.btn_editar.config(state="disabled")
		self.btn_eliminar.config(state="disabled")
		self.entry_obra_social.config(state="disabled")
		self.btn_actualizar.config(state="disabled")
		
	def habilitar_botones_App(self):
		self.btn_agregar.config(state="normal")
		self.btn_editar.config(state="normal")
		self.btn_eliminar.config(state="normal")
		self.entry_obra_social.config(state="normal")
		self.btn_actualizar.config(state="normal")
		
	def get_datos_treeview(self):
		focus_item = self.tabla.focus()
		print(self.tabla.item(focus_item))
		self.afil_target = self.tabla.item(focus_item)["values"]
		print(self.afil_target)
		self.text_info.set("AFILIADO")

	def agregar_afiliado(self):
		print("agregar")

	def editar_afiliado(self):
		print("editar")

	def eliminar_afiliado(self):
		print("eliminar")

	def actualizar(self):
		print("actualizar")


	def ordenar_lista_afiliados(self):
		self.afiliados_sort= sorted(self.afiliados)

	def salir_top_level(self):

		self.top_level.destroy() 
		self.habilitar_botones_App()
		
		

	def get_apellido(self):
		return self.apellido.get()

	def get_afiliados_sort(self):
		return self.afiliados_sort

	def get_obrasocial(self):
		return self.current_obrasocial

	
def app():
	v = App()
	v.root.mainloop()
	
if __name__ == "__main__":
	app()