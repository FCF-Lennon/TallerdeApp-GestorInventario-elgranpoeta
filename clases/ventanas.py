from cProfile import label
import fractions
from re import MULTILINE
from sqlite3 import Cursor
from struct import pack
from tkinter import *
from tkinter import messagebox
from turtle import right, width

from mysqlx import Column
from clases.libros import Libro
from clases.usuario import Usuario
from clases.categoria import Categoria
from clases.editorial import Editorial
from clases.bodega import Bodega

from tkinter import ttk
from tkinter import messagebox as Messagebox

# Ventana de Inicio de Sesion


def ventana_login():
    # Funcion validar llama a la funcion iniciarSesion o IniciarSesionAdmin de la clase Usuario
    # enviandole 2 variables(user,password), despues guarda la lista que le retorna
    # obteniendo el nombre el cual se encuentra en la posicion [2] de la tupla
    # para posteriormente guardarlo en una variable dependiendo del resultado
    # muestra un pop-up deoendiendo de los datos ingresados
    # y finalmente retorna una ventana dependiendo de si la cuenta ingresada es usuario natural o usuario Admin
    def validar():
        try:
            u = Usuario(user.get(), password.get())
            userAdm = u.iniciarSesionAdmin()
            if userAdm:
                global userNameAdm
                userNameAdm = userAdm[2]
                Messagebox.showinfo("Informacion", "Se ha iniciado sesion")
                ventanaInicio.destroy()
                return ventanaMain()
            else:
                userNormal = u.iniciarSesion()
                if userNormal:
                    global userName
                    userName = userNormal[2]
                    Messagebox.showinfo("Informacion", "Se ha iniciado sesion")
                    ventanaInicio.destroy()
                    return ventanaUser()
                return Messagebox.showwarning(
                    "Advertencia", "Rut o contraseña incorrectos"
                )

        except:
            Messagebox.showerror("Error", "Usuario no encontrado")

    def ocultarInfo():
        frm_two.grid_forget()

    def mostrarInfo():
        frm_two.grid(column=1, row=0, sticky='nsew')

    # Instanciación de la ventqna de inicio de sesión
    ventanaInicio = Tk()
    ventanaInicio.title("El gran poeta")
    ventanaInicio.configure(background='#ec7225')
    ventanaInicio.eval('tk::PlaceWindow . center')
    ventanaInicio.iconbitmap("img/logo.ico")
    ventanaInicio.resizable(0, 0)

    # Instanciación de Variables
    user = StringVar()
    password = StringVar()

    # Frames de la ventana de inicio de sesión

    frm_one = Frame(ventanaInicio, bg='#ec7225')
    frm_one.grid(column=0, row=0, pady=2)

    frm_help = Frame(frm_one, bg='white')
    frm_help.pack(fill='x')

    frm_logo = Frame(frm_one, bg='#ec7225')
    frm_logo.pack()

    frm_login = Frame(frm_one, bg='#ec7225')
    frm_login.pack(expand=True, fill='x')

    frm_panel_login = LabelFrame(
    frm_login, text="Login", bg='#ec7225', fg='white', font=("Arial", 20))
    frm_panel_login.pack(expand=True, fill='x', padx=20, ipady=3)

    frm_button = Frame(frm_login, bg='#ec7225')
    frm_button.pack(expand=True, fill='x')

    # Label de la ventanaInicio

    logo = PhotoImage(file=("Img/logo150x150.png"))
    lbl__logo = Label(frm_logo, image=logo, bg='#ec7225')
    lbl__logo.grid(column=0, row=0, pady=5)

    labelUser = Label(
        frm_panel_login, 
        text="Usuario",
        anchor="w", 
        bg='#ec7225', 
        fg='white')
    labelUser.grid(column=0, row=0, sticky='nswe', padx=3)

    labelPass = Label(
        frm_panel_login, 
        text="Contraseña",
        bg='#ec7225', 
        anchor="w", 
        fg='white')
    labelPass.grid(column=0, row=2, sticky='nswe', padx=3)

    # Entry de la VentanaInicio
    entryUser = Entry(
        frm_panel_login, 
        width=27,
        relief='flat', 
        textvariable=user)
    entryUser.grid(column=0, row=1, padx=3, sticky='nswe')
    entryUser.focus()

    entryPass = Entry(
        frm_panel_login, 
        show="*", width=27,
        relief='flat', 
        textvariable=password)
    entryPass.grid(column=0, row=3, padx=3, sticky='nswe')

    # Botones de la ventanaInicio
    # Este boton llama a la funcion validar
    btn_help = Button(
        frm_help,
        text='Mesa de Ayuda',
        height=1,
        border=0,
        bg='white',
        fg='#515a5a',
        activeforeground='#ec7225',
        activebackground='white',
        cursor='hand2',
        command=mostrarInfo)
    btn_help.pack(side=RIGHT, padx=2)

    botonLogin = Button(frm_button, text='LOG IN',
                        command=validar, width=24, cursor='hand2')
    botonLogin.config(
        relief=GROOVE,
        height=1,
        border=0,
        cursor='hand2',
        bg='#515a5a',
        fg='white',
        activebackground='white',
        activeforeground='#ec7225')
    botonLogin.pack(pady=8, padx=20)

    ''' FRAME -------------- '''

    frm_two = Frame(ventanaInicio, bg='white')
    frm_two.grid_forget()

    frm_Registrar = Frame(frm_two, bg='white')
    frm_Registrar.pack(expand=True, fill=BOTH, padx=20)

    frm_btn_volver = Frame(frm_two, bg='white', width=24)
    frm_btn_volver.pack(expand=True, fill=BOTH, padx=20)

    # Con esto mantenemos en ciclo a la  ventana

    ''' LABEL INFOMACION -------------- '''

    lbl_Informacion = Label(
        frm_Registrar, 
        text='Información:', 
        font=('Arial', 20), 
        anchor='w', 
        bg='white', 
        fg='#ec7225', 
        cursor='hand2')
    lbl_Informacion.grid(column=0, row=0, sticky='we')

    lbl_info_one = Label(
        frm_Registrar, 
        text='Apertura de Cuenta:',
        anchor='w', 
        bg='white', 
        fg='#515a5a')
    lbl_info_one.grid(column=0, row=1, sticky='w')
    lbl_info_one_sms = Label(
        frm_Registrar, 
        width=24, 
        relief='flat',
        bg='#f0f0f0', 
        text='llamar a 800 600 5526', 
        fg='#515a5a')
    lbl_info_one_sms.grid(column=0, row=2)

    lbl_info_two = Label(
        frm_Registrar, 
        text='Recuperar Contraseña:',
        anchor='w', 
        bg='white', 
        fg='#515a5a')
    lbl_info_two.grid(column=0, row=3, sticky='w')
    lbl_info_two_sms = Label(
        frm_Registrar, 
        width=24, 
        relief='flat',
        bg='#f0f0f0', 
        text='llamar a 800 600 5528 ', 
        fg='#515a5a')
    lbl_info_two_sms.grid(column=0, row=4)

    lbl_info_three = Label(
        frm_Registrar, 
        text='Cuenta Bloqueda:', 
        anchor='w', 
        bg='white', 
        fg='#515a5a')
    lbl_info_three.grid(column=0, row=5, sticky='w')
    lbl_info_three_sms = Label(
        frm_Registrar, 
        width=24, 
        relief='flat',
        bg='#f0f0f0', 
        text='llamar a 800 600 5530 ', 
        fg='#515a5a')
    lbl_info_three_sms.grid(column=0, row=6)

    lbl_info_four = Label(
        frm_Registrar, text='Para Soporte:',
        anchor='w', 
        bg='white', 
        fg='#515a5a')
    lbl_info_four.grid(column=0, row=7, sticky='w')
    lbl_info_four_sms_one = Label(
        frm_Registrar, 
        width=24, 
        relief='flat',
        bg='#f0f0f0', 
        text='llamar a 800 600 5532', 
        fg='#515a5a')
    lbl_info_four_sms_one.grid(column=0, row=8)

    lbl_info_email = Label(
        frm_Registrar, 
        text='Email:',
        anchor='w', 
        bg='white', 
        fg='#515a5a')
    lbl_info_email.grid(column=0, row=9, sticky='w')
    lbl_info_three_sms_three = Label(
        frm_Registrar, 
        width=24, 
        relief='flat',
        bg='#f0f0f0', 
        text='mesadeayuda@elgranpoeta.cl', 
        fg='#ec7225')
    lbl_info_three_sms_three.grid(column=0, row=10)

    ''' BUTTON -------------- '''

    btn_volver = Button(
        frm_btn_volver,
        text='<< volver',
        relief=GROOVE,
        bg='#515a5a',
        fg='white',
        border=0,
        cursor='hand2',
        command=ocultarInfo,
        activebackground='#ec7225',
        activeforeground='white')
    btn_volver.grid(column=1, row=0, sticky='w', ipadx=6)

    ventanaInicio.mainloop()


# Ventana Principal
def ventanaMain():
    # Equipo de Limpieza
    def conserje():
        codigo.set("")
        nombre.set("")
        autor.set("")
        stock.set("")
        categoria.set("")
        editorial.set("")
        bodega.set("")
    # Equipo de contruccion

    def cerrarSesion():
        ventana_main.destroy()
        ventana_login()

    def actualizar():
        frmCRUDLibros()
    # Frames del menu de opciones

    def frmCRUDLibros():
        desactivar()
        libro = Libro()
        listar = libro.listarLibros()
        for widget in ventana_main.winfo_children():
            widget.pack_forget()

        for i in tabla.get_children():
            tabla.delete(i)
        ventana_main.update()

        conserje()

        frmForm.pack()
        frameListar.pack()
        frameTabla.pack()

        contador = 0
        for l in listar:
            tabla.insert(
                parent="",
                index="end",
                iid=contador,
                values=(l[0], l[1], l[2], l[3], l[4], l[5], l[6]),
            )
            contador += 1

    # Instanciación de la ventana principal
    ventana_main = Tk()
    ventana_main.title(f"El Gram Poeta {userNameAdm} Administrador")
    ventana_main.iconbitmap("img/icon.ico")
    ventana_main.geometry("1350x500")
    ventana_main.resizable(0, 0)

    def registrar():

        try:
            resultado = categoria.get().split(sep=" ")
            CatId = resultado[0]
            resultado2 = editorial.get().split(sep=" ")
            EditId = resultado2[0]
            resultado3 = bodega.get().split(sep=" ")
            BodeId = resultado3[0]

            # Valida que el nombre no pase 70 caracteres

            if len(nombre.get()) < 70:
                libro = Libro(codigo, nombre.get(),
                autor.get(), CatId, stock.get(), EditId, BodeId)
                mensaje = libro.insertarLibro()
                if mensaje:
                    messagebox.showinfo("Registrado", mensaje)
                    conserje()

        except:
            messagebox.showerror("Error", "Debe ingresar datos válidos.")

    def editarLibro():
        try:
            resultado = categoria.get().split(sep=" ")
            CatId = resultado[0]
            resultado2 = editorial.get().split(sep=" ")
            EditId = resultado2[0]
            resultado3 = bodega.get().split(sep=" ")
            BodeId = resultado3[0]

            libro = Libro(codigo.get(), nombre.get(),
            autor.get(), CatId, stock.get(), EditId, BodeId)
            mensaje = libro.editarLibro()
            if mensaje:
                messagebox.showinfo("Editado", mensaje)
                conserje()
        except:
            messagebox.showerror("Error", "Debe ingresar datos válidos.")

    def editar():
        conserje()
        try:
            codigo_libro = tabla.item(tabla.selection())['values'][0]
            categoria_libro = tabla.item(tabla.selection())['values'][1]
            nombre_libro = tabla.item(tabla.selection())['values'][2]
            autor_libro = tabla.item(tabla.selection())['values'][3]
            stock_libro = tabla.item(tabla.selection())['values'][4]
            editorial_libro = tabla.item(tabla.selection())['values'][5]
            bodega_libro = tabla.item(tabla.selection())['values'][6]

            habilitar()
            botonRegistrar.config(state='disabled')
            botonCancelar.config(state='disabled')
            entryCodigo.config(state='normal')

            entryCodigo.insert(0, codigo_libro)
            entryCodigo.config(state='disabled')
            entryNombre.insert(0, nombre_libro)
            entryAutor.insert(0, autor_libro)
            entryStock.insert(0, stock_libro)
            comboBoxEditorial.insert(0, editorial_libro)
            comboBoxBodega.insert(0, bodega_libro)
            comboBoxCategoria.set(categoria_libro)
        except:
            pass

    def eliminar():
        try:
            libro = Libro(codigo.get())
            mensaje = libro.eliminarLibro()
            if mensaje:
                messagebox.showinfo("Eliminado", mensaje)
                conserje()
        except:
            messagebox.showerror("Error", "Debe ingresar datos válidos.")

    def habilitar():
        entryCodigo.config(state='normal')
        entryNombre.config(state='normal')
        entryAutor.config(state='normal')
        entryStock.config(state='normal')
        comboBoxEditorial.config(state='normal')
        comboBoxBodega.config(state='normal')
        comboBoxCategoria.config(state='readonly')

        botonRegistrar.config(state='normal')
        botonCancelar.config(state='normal')
        botonActualizarLibro.config(state='normal')
        botonEliminar.config(state='normal')

    def desactivar():
        entryCodigo.config(state='disabled')
        entryNombre.config(state='disabled')
        entryAutor.config(state='disabled')
        entryStock.config(state='disabled')
        comboBoxEditorial.config(state='disabled')
        comboBoxBodega.config(state='disabled')
        comboBoxCategoria.config(state='disabled')

        botonRegistrar.config(state='disabled')
        botonCancelar.config(state='disabled')
        botonActualizarLibro.config(state='disabled')
        botonEliminar.config(state='disabled')
        conserje()

        # HAY QUE REVISAR ESTO

    def BuscarLibros():
        bodega = bodega.get().split(sep=" ") 
        bodegaId = bodega[0]
        
        try:
            libro = Libro(  
                bodegaId
                            )
            listar = libro.buscarLibro()
            for l in listar:
                nombre.set(l[1])
                autor.set(l[2])
                stock.set(l[3])
                categoria.set(l[4])
                editorial.set(l[5])
                bodega.set(l[6])
        except:
            messagebox.showerror("Error", "No se pudo encontrar el libro.")
            conserje()

    # Menu de opciones
    menubar = Menu(ventana_main)
    ventana_main.config(menu=menubar)

    createmenuOpciones = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Opciones", menu=createmenuOpciones)
    createmenuOpciones.add_command(
        label="Libros", command=frmCRUDLibros)

    createmenuPerfil = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Perfil", menu=createmenuPerfil)
    createmenuPerfil.add_command(label="Editar Perfil")
    
    createmenuPerfil.add_command(label="Ver Perfil")

    createmenuAyuda = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ayuda", menu=createmenuAyuda)
    createmenuAyuda.add_command(label="Soporte Tecnico")
    createmenuAyuda.add_command(
        label="Reportar Problema")
    createmenuAyuda.add_command(label="Cerrar Sesion", command=cerrarSesion)
    createmenuAyuda.add_command(label="Salir", command=ventana_main.destroy)

    # Variables
    codigo = StringVar()
    categoria = StringVar()
    nombre = StringVar()
    autor = StringVar()
    stock = StringVar()
    editorial = StringVar()
    bodega = StringVar()

    # Frame para listar los libros
    frameListar = Frame(ventana_main)

    # Frame de la tabla de libros
    frameTabla = Frame(frameListar)
    frameTabla.pack()
    tabla = ttk.Treeview(frameTabla, selectmode="browse", height=8)
    tabla.pack(side="left")
    # Scroll de frameTabla
    scroll = ttk.Scrollbar(frameTabla, orient='vertical', command=tabla.yview)
    scroll.pack(side="right", fill="both")

    tabla["columns"] = ("Codigo", "Categoria", "Nombre",
                        "Autor", "Stock", "Editorial", "Bodegas")
    tabla.column("#0", width=0, stretch=NO)
    tabla.column("#1", width = 80, anchor = 'e')
    tabla.column("#2", width = 80, anchor = 'e')
    tabla.column("#3", width = 80, anchor = 'e')
    tabla.column("#4", width = 80, anchor = 'e' )
    tabla.column("#5", width = 85, anchor = 'e')
    tabla.column("#6", width = 85, anchor = 'e')
    tabla.column("#7", width = 70, anchor = 'e')

    tabla.heading("Codigo", text="Codigo", anchor=CENTER)
    tabla.heading("Categoria", text="Categoria", anchor=CENTER)
    tabla.heading("Nombre", text="Nombre", anchor=CENTER)
    tabla.heading("Autor", text="Autor", anchor=CENTER)
    tabla.heading("Stock", text="Stock", anchor=CENTER)
    tabla.heading("Editorial", text="Editorial", anchor=CENTER)
    tabla.heading("Bodegas", text="Bodegas", anchor=CENTER)

    tabla.configure(show='headings', yscrollcommand=scroll.set)

    # Botones del frameTabla

    botonBuscar = Button(frameTabla, text='Buscar Libro', command=BuscarLibros)
    botonBuscar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#158645', 
        cursor='hand2', 
        activebackground='#35BD6F')
    botonBuscar.grid(column=0, row=0, sticky="nwe", pady=5, padx=5)

    botonEditar = Button(frameTabla, text='Editar Libro', command=editar)
    botonEditar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#158645', 
        cursor='hand2', 
        activebackground='#35BD6F')
    botonEditar.grid(column=1, row=0, sticky="nwe", pady=5, padx=5)

    botonActualizar = Button(
        frameTabla, text='Actualizar Tabla', command=actualizar)
    botonActualizar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#1658A2', 
        cursor='hand2', 
        activebackground='#3586DF')
    botonActualizar.grid(column=2, row=0, sticky="nwe", pady=5, padx=5)

    botonActualizarLibro = Button(
        frameTabla, 
        text='Actualizar Libro', 
        command=editarLibro)
    botonActualizarLibro.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#1658A2', 
        cursor='hand2', 
        activebackground='#3586DF')
    botonActualizarLibro.grid(column=3, row=0, sticky="nwe", pady=5, padx=5)

    botonEliminar = Button(frameTabla, text="Eliminar Libro", command=eliminar)
    botonEliminar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#BD152E', 
        cursor='hand2', 
        activebackground='#E15370')
    botonEliminar.grid(column=4, row=0, sticky="nwe", pady=5, padx=5)

    # Frame para ingresar libros

    frmForm = Frame(frameListar)
    frmForm.grid(row=0, column=0, sticky='nsew')

    frm_menu_registro = Frame(frmForm)
    frm_menu_registro.grid(row=0, column=0, sticky='nsew')

    # Label del Frame frmForm
    labelCodigo = Label(frm_menu_registro, text="ISBN")
    labelCodigo.config(font=('Arial', 12, 'bold'))
    labelCodigo.grid(column=0, row=0, pady=5, padx=5, sticky="w")

    labelNombre = Label(frm_menu_registro, text="Nombre")
    labelNombre.config(font=('Arial', 12, 'bold'))
    labelNombre.grid(column=0, row=1, pady=5, padx=5, sticky="w")

    labelAutor = Label(frm_menu_registro, text="Autor")
    labelAutor.config(font=('Arial', 12, 'bold'))
    labelAutor.grid(column=0, row=2, pady=5, padx=5, sticky="w")

    labelStock = Label(frm_menu_registro, text="Stock")
    labelStock.config(font=('Arial', 12, 'bold'))
    labelStock.grid(column=0, row=3, pady=5, padx=5, sticky="w")

    labelCategoria = Label(frm_menu_registro, text="Categoria")
    labelCategoria.config(font=('Arial', 12, 'bold'))
    labelCategoria.grid(column=0, row=4, pady=5, padx=5, sticky="w")

    labelEditorial = Label(frm_menu_registro, text="Editorial")
    labelEditorial.config(font=('Arial', 12, 'bold'))
    labelEditorial.grid(column=0, row=5, pady=5, padx=5, sticky="w")

    labelBodegas = Label(frm_menu_registro, text="Bodegas")
    labelBodegas.config(font=('Arial', 12, 'bold'))
    labelBodegas.grid(column=0, row=6, pady=5, padx=5, sticky="w")

    # Entry del Frame frmForm
    entryCodigo = Entry(frm_menu_registro, textvariable=codigo)
    entryCodigo.grid(column=1, row=0, pady=5, padx=5)

    entryNombre = Entry(frm_menu_registro, textvariable=nombre)
    entryNombre.grid(column=1, row=1, pady=5, padx=5)

    entryAutor = Entry(frm_menu_registro, textvariable=autor)
    entryAutor.grid(column=1, row=2, pady=5, padx=5)

    entryStock = Entry(frm_menu_registro, textvariable=stock)
    entryStock.grid(column=1, row=3, pady=5, padx=5)


    # Instancia de la clase Categoria
    c = Categoria()
    # Lista de generos para el comboBoxCategoria
    lista = c.listarCategorias()

    # Combobox del Frame frmForm
    comboBoxCategoria = ttk.Combobox(
        frm_menu_registro, values=lista, textvariable=categoria)
    comboBoxCategoria.grid(column=1, row=4, pady=5)

    # Instancia de la clase Editorial
    e = Editorial()
    # Lista de generos para el comboBoxEditorial
    listas = e.listarEditorial()

    # Combobox del Frame frmForm
    comboBoxEditorial = ttk.Combobox(
        frm_menu_registro, values=listas, textvariable=editorial)
    comboBoxEditorial.grid(column=1, row=5, pady=5)

    # Instancia de la clase Bodega
    b = Bodega()
    # Lista de generos para el comboBoxBodega
    listas = b.listarBodega()

    # Combobox del Frame frmForm

    comboBoxBodega = ttk.Combobox(
        frm_menu_registro, values=listas, textvariable=bodega)
    comboBoxBodega.grid(column=1, row=6, pady=5)

    
    # Botones del Frame frmForm
    botonNuevo = Button(frm_menu_registro, text="Nuevo Registro", command=habilitar)
    botonNuevo.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#158645', 
        cursor='hand2', 
        activebackground='#35BD6F')
    botonNuevo.grid(column=0, row=7, sticky="w", pady=2, padx=5, columnspan=2)

    botonRegistrar = Button(frm_menu_registro, text="Registrar", command=registrar)
    botonRegistrar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#1658A2', 
        cursor='hand2', 
        activebackground='#3586DF')
    botonRegistrar.grid(column=0, row=8, sticky="w", pady=2, padx=5)

    botonCancelar = Button(frm_menu_registro, text="Cancelar", command=desactivar)
    botonCancelar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#BD152E', 
        cursor='hand2', 
        activebackground='#E15370')
    botonCancelar.grid(column=1, row=8, sticky="w", pady=2, padx=5)

    # Frame para editar libros
    frameEditar = Frame(ventana_main)
    frmTituloEditar = Frame(frameEditar)
    frmTituloEditar.pack()
    Label(frmTituloEditar, text="Editar Libros", font=("Arial", 20)).pack()

    frmFormEditar = Frame(frameEditar)
    frmFormEditar.pack(padx=60, pady=5)

    Label(frmFormEditar, text="Codigo del Libro").grid(
        column=0, row=0, pady=5, padx=5, sticky="w"
    )
    Entry(frmFormEditar, textvariable=codigo).grid(
        column=0, row=1, pady=5, padx=5, sticky="w"
    )

    Label(frmFormEditar, text="Nombre").grid(
        column=1, row=0, pady=5, padx=5, sticky="w"
    )
    Entry(frmFormEditar, textvariable=nombre).grid(
        column=1, row=1, pady=5, padx=5, sticky="w"
    )

    Label(frmFormEditar, text="Autor").grid(
        column=2, row=0, pady=5, padx=5, sticky="W")
    Entry(frmFormEditar, textvariable=autor).grid(
        column=2, row=1, pady=5, padx=5, sticky="w"
    )

    Label(frmFormEditar, text="Stock").grid(
        column=3, row=0, pady=5, padx=5, sticky="w")
    Entry(frmFormEditar, textvariable=stock).grid(
        column=3, row=1, pady=5, padx=5, sticky="w"
    )

    Label(frmFormEditar, text="Categoria").grid(
        column=4, row=0, pady=5, padx=5, sticky="w"
    )
    Entry(frmFormEditar, textvariable=categoria).grid(
        column=4, row=1, pady=5, padx=5, sticky="w"
    )
    Label(frmFormEditar, text="Editorial").grid(
        column=4, row=0, pady=5, padx=5, sticky="w"
    )
    Entry(frmFormEditar, textvariable=editorial).grid(
        column=4, row=1, pady=5, padx=5, sticky="w"
    )

    Label(frmFormEditar, text="Bodega").grid(
        column=4, row=0, pady=5, padx=5, sticky="w"
    )
    Entry(frmFormEditar, textvariable=bodega).grid(
        column=4, row=1, pady=5, padx=5, sticky="w"
    )

    Button(frmFormEditar, text="buscar", command=BuscarLibros).grid(
        column=5, row=3, pady=5, padx=5, sticky="w"
    )
    ventana_main.mainloop()

# Ventana Usuario


def ventanaUser():
    # Equipo de contruccion
    def bobContructor():
        for widget in ventana_user.winfo_children():
            widget.pack_forget()
        frmContruccion = Frame(ventana_user)
        frmContruccion.pack()

        labelTitulo = Label(frmContruccion, text="BOB's CONTRUCTION SITE")
        labelTitulo.config(font=('Arial', 40, 'bold'))
        labelTitulo.pack()

        labelBob = Label(
            frmContruccion, text="Hola como el ingeniero responsable de esta obra lamenteo informarle que")
        labelBob.config(font=('Arial', 12, 'bold'))
        labelBob.pack()

        labelBob2 = Label(
            frmContruccion, text="estamos atrasados, disculpe por la demora por eso aqui le dejo nuestra canción")
        labelBob2.config(font=('Arial', 12, 'bold'))
        labelBob2.pack()

        labelCancion = Label(
            frmContruccion, text="Bob construye ¿Podran hacerlo? Bob construye ¡SI PODREMOS!")
        labelCancion.config(font=('Arial', 9, 'bold'))
        labelCancion.pack()

        labelCancion2 = Label(
            frmContruccion, text="Scoop, Mot y Disy y Rolly tambien Lofty y Wendy lo ayudan bien son un gran equipo al trabajar y se divierten al terminar")
        labelCancion2.config(font=('Arial', 9, 'bold'))
        labelCancion2.pack()

        labelCancion3 = Label(
            frmContruccion, text="Bob construye ¿Podran hacerlo? Bob construye ¡SI PODREMOS!")
        labelCancion3.config(font=('Arial', 9, 'bold'))
        labelCancion3.pack()

        labelCancion4 = Label(
            frmContruccion, text="Pincha y una ave, Travis y Spot juegan contentos amigos son")
        labelCancion4.config(font=('Arial', 9, 'bold'))
        labelCancion4.pack()

        labelCancion5 = Label(
            frmContruccion, text="Bob construye ¿Podran hacerlo? Bob construye ¡SI PODREMOS!")
        labelCancion5.config(font=('Arial', 9, 'bold'))
        labelCancion5.pack()

        labelIngeniero = Label(
            frmContruccion, text="¡MUCHAS GRACIAS BANDA AHI NOS VEMOS!")
        labelIngeniero.config(font=('Arial', 20, 'bold'))
        labelIngeniero.pack()

    def cerrarSesion():
        ventana_user.destroy()
        ventana_login()

    def Libros():
        libro = Libro()
        listar = libro.listarLibros()
        for widget in ventana_user.winfo_children():
            widget.pack_forget()

        frameListar.pack()
        frameTabla.pack()

        for i in tabla.get_children():
            tabla.delete(i)
        ventana_user.update()

        contador = 0
        for l in listar:
            tabla.insert(
                parent="",
                index="end",
                iid=contador,
                values=(l[1], l[2], l[3]),
            )
            contador += 1

    ventana_user = Tk()
    ventana_user.title(f"Biblioteca de {userName}")
    ventana_user.geometry("1100x500")
    ventana_user.resizable(0, 0)

    # Menu de opciones
    menubar = Menu(ventana_user)
    ventana_user.config(menu=menubar)

    createmenuOpciones = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Opciones", menu=createmenuOpciones)
    createmenuOpciones.add_command(
        label="Ver Libros Disponibles", command=Libros)
    createmenuOpciones.add_command(
        label="Arrendar Libros")

    createmenuPerfil = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Perfil", menu=createmenuPerfil)
    createmenuPerfil.add_command(label="Editar Perfil")
    createmenuPerfil.add_command(
        label="Libros Arrendados")
    createmenuPerfil.add_command(label="Ver Perfil")

    menubar.add_command(label="Configuracion")

    createmenuAyuda = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ayuda", menu=createmenuAyuda)
    createmenuAyuda.add_command(label="Soporte Tecnico")
    createmenuAyuda.add_command(
        label="Reportar Problema")
    createmenuAyuda.add_command(label="Cerrar Sesion", command=cerrarSesion)
    createmenuAyuda.add_command(label="Salir", command=ventana_user.destroy)
    # Frame para listar los libros
    frameListar = Frame(ventana_user)
    # Frame de la tabla de libros
    frameTabla = Frame(frameListar)
    tabla = ttk.Treeview(frameTabla)
    tabla.grid(row=5, column=0, columnspan=5, sticky='nse')

    # Scroll de frameTabla
    scroll = ttk.Scrollbar(frameTabla, orient='vertical', command=tabla.yview)
    scroll.grid(row=5, column=5, sticky='nse')
    tabla.config(yscrollcommand=scroll.set)

    tabla["columns"] = ("Categoria", "Nombre", "Autor")
    tabla.column("#0", width=0, stretch=NO)
    tabla.heading("Categoria", text="Categoria", anchor=CENTER)
    tabla.heading("Nombre", text="Nombre", anchor=CENTER)
    tabla.heading("Autor", text="Autor", anchor=CENTER)
    ventana_user.mainloop()
