from cProfile import label
from tkinter import *
from tkinter import messagebox

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
            print(userAdm, 'linea 28 ventanas')
            if userAdm:
                global userNameAdm
                userNameAdm = userAdm[2]
                print(userAdm[2], 'linea 32 ventanas')
                Messagebox.showinfo("Informacion", "Se ha iniciado sesion")
                print(userNameAdm, 'linea 34 ventanas')
                ventanaInicio.destroy()
                return ventanaMain()
        except:
            Messagebox.showerror("Error", "Usuario no encontrado")

    def ocultarInfo():
        frm_two.grid_forget()

    def mostrarInfo():
        frm_two.grid(column=1, row=0, sticky='nsew')


    # Instanciación de la ventqna de inicio de sesión
    ventanaInicio = Tk()
    ventanaInicio.title("El gran poeta - ")
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

    def cerrarSesion():
        ventana_main.destroy()
        ventana_login()

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

    def conserje():
        codigo.set("")
        nombre.set("")
        autor.set("")
        stock.set("")
        categoria.set("")
        editorial.set("")
        bodega.set("")

    def actualizar():
        libro = Libro()
        listar = libro.listarLibros()

        for widget in ventana_main.winfo_children():
            widget.pack_forget()

        for i in tabla.get_children():
            tabla.delete(i)

        ventana_main.update()
        contador = 0

        for l in listar:
            tabla.insert(
                parent="",
                index="end",
                iid=contador,
                values=(l[0], l[1], l[2], l[3], l[4], l[5], l[6]),
            )
            contador += 1

        frameListar.pack(side='left')
        frameTabla.pack(side='right')

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
            # pendiente
    def BuscarLibros():
        
        try:
            if codigo.get() != '':
                libro = Libro(
                codigo.get()
                )

                listar = libro.buscarLibro()

                for l in listar:
                    nombre.set(l[1])
                    autor.set(l[2])
                    stock.set(l[3])
                    categoria.set(l[4])
                    editorial.set(l[5])
                    bodega.set(l[6])

            else:
                messagebox.showerror("Error", "No hay parametros de busqueda")
        except:

            messagebox.showerror("Error", "No se pudo encontrar el libro.")

            conserje()
    
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
        conserje()
    
    def eliminar():
        try:
            if codigo.get() != '':
                libro = Libro(codigo.get())
                mensaje = libro.eliminarLibro()
                if mensaje:
                    messagebox.showinfo("Eliminado", mensaje)
                    conserje()
            else:
                messagebox.showerror("Error", "No hay parametros de busqueda")
        except:
            messagebox.showerror("Error", "Debe ingresar datos válidos.")

    def editarLibro():
        try:
            if codigo.get() != '':
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
            else:
                messagebox.showerror("Error", "No hay parametros de busqueda")
        except:
            messagebox.showerror("Error", "Debe ingresar datos válidos.")

    # Instanciación de la ventana principal
    ventana_main = Tk()
    ventana_main.title(f"El Gram Poeta {userNameAdm} Administrador") 
    """ print(userNameAdm, 'linea 318 de ventanas') """
    """ ventana_main.iconbitmap("img/icon.ico") """ 
    ventana_main.resizable(0, 0) 

    """ MENU """

    menubar = Menu(ventana_main)
    ventana_main.config(menu=menubar)

    createmenuOpciones = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Opciones", menu=createmenuOpciones)

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


    """ Definir las variables - campos de texto  y combobox en ventana """

    codigo = StringVar()
    categoria = StringVar()
    nombre = StringVar()
    autor = StringVar()
    stock = StringVar()
    editorial = StringVar()
    bodega = StringVar()

    """ MENU INGRESAR LIBRO """

    # Frame para listar los libros
    frameListar = Frame(ventana_main, width=30)

    # Frame para ingresar libros

    frmForm = Frame(frameListar, bg='#ec7225')
    frmForm.grid(row=0, column=0, sticky='nsew')


    frm_menu_registro = Frame(frmForm, bg='#ec7225')
    frm_menu_registro.grid(row=1, column=0, sticky='nsew')

    frm_menu_labels = Frame(frm_menu_registro, bg='#ec7225', width=20)
    frm_menu_labels.grid(row=0, column=0, sticky='nsew')

    frm_menu_cajas = Frame(frm_menu_registro, bg='#ec7225', width=10)
    frm_menu_cajas.grid(row=0, column=1, sticky='nsew', pady=2)

    frm_menu_botones = Frame(frm_menu_registro, bg='#ec7225', width=10)
    frm_menu_botones.grid(row=4, column=0, sticky='nsew', columnspan=2)

    # Label del Frame frmForm

    labeltitulo= Label(frmForm, text="El Gran Poeta", font=("Arial", 15), bg='#ec7225', fg='white')
    labeltitulo.grid(row=0, column=0, sticky='nsew')
    labelCodigo = Label(frm_menu_labels, text="ISBN", bg='#ec7225', fg='white')
    labelCodigo.grid(column=0, row=1, sticky="w")
    labelNombre = Label(frm_menu_labels, text="Nombre", bg='#ec7225', fg='white')
    labelNombre.grid(column=0, row=2, sticky="w")
    labelAutor = Label(frm_menu_labels, text="Autor", bg='#ec7225', fg='white')
    labelAutor.grid(column=0, row=3, sticky="w")
    labelStock = Label(frm_menu_labels, text="Stock", bg='#ec7225', fg='white')
    labelStock.grid(column=0, row=4, sticky="w")
    labelCategoria = Label(frm_menu_labels, text="Categoria", bg='#ec7225', fg='white')
    labelCategoria.grid(column=0, row=6, sticky="w")
    labelEditorial = Label(frm_menu_labels, text="Editorial", bg='#ec7225', fg='white')
    labelEditorial.grid(column=0, row=7, sticky="w")
    labelBodegas = Label(frm_menu_labels, text="Bodegas", bg='#ec7225', fg='white')
    labelBodegas.grid(column=0, row=8, sticky="w")

    # Entry del Frame frmForm
    entryCodigo = Entry(frm_menu_cajas, textvariable=codigo)
    entryCodigo.grid(column=1, row=0 , pady=1)

    entryNombre = Entry(frm_menu_cajas, textvariable=nombre)
    entryNombre.grid(column=1, row=1 , pady=1)

    entryAutor = Entry(frm_menu_cajas, textvariable=autor)
    entryAutor.grid(column=1, row=2 , pady=1)

    entryStock = Entry(frm_menu_cajas, textvariable=stock)
    entryStock.grid(column=1, row=3 , pady=1)

    # Instancia de la clase Categoria
    c = Categoria()
    # Lista de generos para el comboBoxCategoria
    lista = c.listarCategorias()

    # Combobox del Frame frmForm
    comboBoxCategoria = ttk.Combobox(
        frm_menu_cajas, values=lista, textvariable=categoria, width=17)
    comboBoxCategoria.grid(column=1, row=4, pady=1)

    # Instancia de la clase Editorial
    e = Editorial()
    # Lista de generos para el comboBoxEditorial
    listas = e.listarEditorial()

    # Combobox del Frame frmForm
    comboBoxEditorial = ttk.Combobox(
        frm_menu_cajas, values=listas, textvariable=editorial, width=17)
    comboBoxEditorial.grid(column=1, row=5, pady=1)

    # Instancia de la clase Bodega
    b = Bodega()
    # Lista de generos para el comboBoxBodega
    listas = b.listarBodega()

    # Combobox del Frame frmForm

    comboBoxBodega = ttk.Combobox(
        frm_menu_cajas, values=listas, textvariable=bodega, width=17)
    comboBoxBodega.grid(column=1, row=6, pady=1)

    # Botones del Frame frmForm
    botonNuevo = Button(frm_menu_registro, text="Nuevo Registro", command=habilitar, relief=GROOVE)
    botonNuevo.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#158645', 
        cursor='hand2', 
        activebackground='#35BD6F')
    botonNuevo.grid(column=0, row=7, sticky="nsew", columnspan=2)

    botonRegistrar = Button(frm_menu_botones, text="Registrar", command=registrar, relief=GROOVE, width=12)
    botonRegistrar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#1658A2', 
        cursor='hand2', 
        activebackground='#3586DF')
    botonRegistrar.grid(column=0, row=0, sticky="w")

    botonCancelar = Button(frm_menu_botones, text="Cancelar", command=desactivar, relief=GROOVE, width=12)
    botonCancelar.config(
        font=('Arial', 8, 'bold'), 
        fg='#DAD5D6',
        bg='#BD152E', 
        cursor='hand2', 
        activebackground='#E15370')
    botonCancelar.grid(column=1, row=0, sticky="w")


    """" TABLA DE LIBROS """

    # Frame de la tabla de libros
    frameTabla = Frame(ventana_main)    

    tabla = ttk.Treeview(frameTabla)
    tabla.grid(row=5, column=0, columnspan=5, sticky='nse')
    # Scroll de frameTabla
    scroll = ttk.Scrollbar(frameTabla, orient='vertical', command=tabla.yview)
    scroll.grid(row=5, column=5, sticky='nse')
    tabla.config(yscrollcommand=scroll.set)

    tabla["columns"] = ("Codigo", "Categoria", "Nombre",
                        "Autor", "Stock", "Editorial", "Bodegas")

    tabla.column("#0", width=0, stretch=NO)
    tabla.column("Codigo", width=100, stretch=NO)
    tabla.column("Categoria", width=100, stretch=NO)
    tabla.column("Nombre", width=100, stretch=NO)
    tabla.column("Autor", width=100, stretch=NO)
    tabla.column("Stock", width=100, stretch=NO)
    tabla.column("Editorial", width=100, stretch=NO)
    tabla.column("Bodegas", width=100, stretch=NO)

    tabla.heading("Codigo", text="Codigo", anchor=CENTER)
    tabla.heading("Categoria", text="Categoria", anchor=CENTER)
    tabla.heading("Nombre", text="Nombre", anchor=CENTER)
    tabla.heading("Autor", text="Autor", anchor=CENTER)
    tabla.heading("Stock", text="Stock", anchor=CENTER)
    tabla.heading("Editorial", text="Editorial", anchor=CENTER)
    tabla.heading("Bodegas", text="Bodegas", anchor=CENTER)


    libro = Libro()
    listar = libro.listarLibros()

    for widget in ventana_main.winfo_children():
        widget.pack_forget()

    for i in tabla.get_children():
        tabla.delete(i)

    ventana_main.update()
    desactivar()
    contador = 0

    for l in listar:
        tabla.insert(
            parent="",
            index="end",
            iid=contador,
            values=(l[0], l[1], l[2], l[3], l[4], l[5], l[6]),
        )
        contador += 1

    frameListar.pack(side='left', padx=5)
    frameTabla.pack(side='right')

    """ desactivar() """

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

    """ ---------------------------- """

    ventana_main.mainloop()

"""
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
)"""

