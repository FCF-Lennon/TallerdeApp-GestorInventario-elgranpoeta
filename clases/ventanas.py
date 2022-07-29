from cProfile import label
from struct import pack
from tkinter import *
from tkinter import messagebox
from clases.libros import Libro
from clases.usuario import Usuario
from clases.categoria import Categoria
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

    # Instanciación de la ventqna de inicio de sesión
    ventanaInicio = Tk()
    ventanaInicio.title("Inicio de Sesión")
    ventanaInicio.geometry("300x300")
    ventanaInicio.resizable(0, 0)

    # Instanciación de Variables
    user = StringVar()
    password = StringVar()

    # Label de la ventanaInicio
    labelInicioSesion = Label(text="Inicio de Sesión")
    labelInicioSesion.config(font=('Arial', 20, 'bold'))
    labelInicioSesion.pack()

    labelUser = Label(text="Usuario")
    labelUser.config(font=('Arial', 15, 'bold'))
    labelUser.place(x=150, y=50, anchor=CENTER)

    labelPass = Label(text="Contraseña")
    labelPass.config(font=('Arial', 15, 'bold'))
    labelPass.place(x=150, y=150, anchor=CENTER)

    # Entry de la VentanaInicio
    entryUser = Entry(textvariable=user)
    entryUser.place(x=150, y=100, anchor=CENTER)

    entryPass = Entry(textvariable=password, show="*")
    entryPass.place(x=150, y=200, anchor=CENTER)

    # Botones de la ventanaInicio

    # Este boton llama a la funcion validar
    botonLogin = Button(text='Continuar', command=validar)
    botonLogin.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                      bg='#1658A2', cursor='hand2', activebackground='#3586DF')
    botonLogin.place(x=100, y=250, anchor=CENTER)

    # Este boton termina la ejecucion del programa
    botonCancelar = Button(text="Cancelar", command=ventanaInicio.destroy)
    botonCancelar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                         bg='#BD152E', cursor='hand2', activebackground='#E15370')
    botonCancelar.place(x=200, y=250, anchor=CENTER)

    # Con esto mantenemos en ciclo a la  ventana
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
    # Equipo de contruccion

    def bobContructor():
        for widget in ventana_main.winfo_children():
            widget.pack_forget()
        frmContruccion = Frame(ventana_main)
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
                values=(l[0], l[1], l[2], l[3], l[4]),
            )
            contador += 1

    # Instanciación de la ventana principal
    ventana_main = Tk()
    ventana_main.title(f"Biblioteca {userNameAdm} Administrador")
    ventana_main.geometry("1100x500")
    ventana_main.resizable(0, 0)

    def registrar():
        try:
            resultado = categoria.get().split(sep=" ")
            Catid = resultado[0]
            libro = Libro(codigo, nombre.get(),
                          autor.get(), Catid, stock.get())
            mensaje = libro.insertarLibro()
            if mensaje:
                messagebox.showinfo("Registrado", mensaje)
                conserje()
        except:
            messagebox.showerror("Error", "Debe ingresar datos válidos.")

    def editarLibro():
        try:
            resultado = categoria.get().split(sep=" ")
            Catid = resultado[0]
            libro = Libro(codigo.get(), nombre.get(),
                          autor.get(), Catid, stock.get())
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

            habilitar()
            botonRegistrar.config(state='disabled')
            botonCancelar.config(state='disabled')
            entryCodigo.config(state='normal')

            entryCodigo.insert(0, codigo_libro)
            entryCodigo.config(state='disabled')
            entryNombre.insert(0, nombre_libro)
            entryAutor.insert(0, autor_libro)
            entryStock.insert(0, stock_libro)
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
        comboBoxCategoria.config(state='disabled')

        botonRegistrar.config(state='disabled')
        botonCancelar.config(state='disabled')
        botonActualizarLibro.config(state='disabled')
        botonEliminar.config(state='disabled')
        conserje()

    def BuscarLibros():

        try:
            libro = Libro(codigo.get())
            listar = libro.buscarLibro()
            for l in listar:
                nombre.set(l[1])
                autor.set(l[2])
                stock.set(l[3])
                categoria.set(l[4])
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
    createmenuPerfil.add_command(label="Editar Perfil", command=bobContructor)
    createmenuPerfil.add_command(
        label="Arriendos de libros", command=bobContructor)
    createmenuPerfil.add_command(label="Ver Perfil", command=bobContructor)

    menubar.add_cascade(label="Configuracion", command=bobContructor)

    createmenuAyuda = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ayuda", menu=createmenuAyuda)
    createmenuAyuda.add_command(label="Soporte Tecnico", command=bobContructor)
    createmenuAyuda.add_command(
        label="Reportar Problema", command=bobContructor)
    createmenuAyuda.add_command(label="Cerrar Sesion", command=cerrarSesion)
    createmenuAyuda.add_command(label="Salir", command=ventana_main.destroy)

    # Variables
    codigo = StringVar()
    categoria = StringVar()
    nombre = StringVar()
    autor = StringVar()
    stock = StringVar()

    # Frame para listar los libros
    frameListar = Frame(ventana_main)
    # Frame de la tabla de libros
    frameTabla = Frame(frameListar)
    tabla = ttk.Treeview(frameTabla)
    tabla.grid(row=5, column=0, columnspan=5, sticky='nse')
    # Scroll de frameTabla
    scroll = ttk.Scrollbar(frameTabla, orient='vertical', command=tabla.yview)
    scroll.grid(row=5, column=5, sticky='nse')
    tabla.config(yscrollcommand=scroll.set)

    tabla["columns"] = ("Codigo", "Categoria", "Nombre", "Autor", "Stock")
    tabla.column("#0", width=0, stretch=NO)
    tabla.heading("Codigo", text="Codigo", anchor=CENTER)
    tabla.heading("Categoria", text="Categoria", anchor=CENTER)
    tabla.heading("Nombre", text="Nombre", anchor=CENTER)
    tabla.heading("Autor", text="Autor", anchor=CENTER)
    tabla.heading("Stock", text="Stock", anchor=CENTER)

    # Botones del frameTabla

    botonBuscar = Button(frameTabla, text='Buscar Libro', command=BuscarLibros)
    botonBuscar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                       bg='#158645', cursor='hand2', activebackground='#35BD6F')
    botonBuscar.grid(column=0, row=7, sticky="nwe", pady=5, padx=5)

    botonEditar = Button(frameTabla, text='Editar Libro', command=editar)
    botonEditar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                       bg='#158645', cursor='hand2', activebackground='#35BD6F')
    botonEditar.grid(column=1, row=7, sticky="nwe", pady=5, padx=5)

    botonActualizar = Button(
        frameTabla, text='Actualizar Tabla', command=actualizar)
    botonActualizar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                           bg='#1658A2', cursor='hand2', activebackground='#3586DF')
    botonActualizar.grid(column=2, row=7, sticky="nwe", pady=5, padx=5)

    botonActualizarLibro = Button(
        frameTabla, text='Actualizar Libro', command=editarLibro)
    botonActualizarLibro.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                                bg='#1658A2', cursor='hand2', activebackground='#3586DF')
    botonActualizarLibro.grid(column=3, row=7, sticky="nwe", pady=5, padx=5)

    botonEliminar = Button(frameTabla, text="Eliminar Libro", command=eliminar)
    botonEliminar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                         bg='#BD152E', cursor='hand2', activebackground='#E15370')
    botonEliminar.grid(column=4, row=7, sticky="nwe", pady=5, padx=5)

    # Frame para ingresar libros
    frmForm = Frame(frameListar)

    # Label del Frame frmForm
    labelCodigo = Label(frmForm, text="Codigo del Libro")
    labelCodigo.config(font=('Arial', 12, 'bold'))
    labelCodigo.grid(column=0, row=0, pady=5, padx=5, sticky="w")

    labelNombre = Label(frmForm, text="Nombre")
    labelNombre.config(font=('Arial', 12, 'bold'))
    labelNombre.grid(column=1, row=0, pady=5, padx=5, sticky="w")

    labelAutor = Label(frmForm, text="Autor")
    labelAutor.config(font=('Arial', 12, 'bold'))
    labelAutor.grid(column=2, row=0, pady=5, padx=5, sticky="w")

    labelStock = Label(frmForm, text="Stock")
    labelStock.config(font=('Arial', 12, 'bold'))
    labelStock.grid(column=3, row=0, pady=5, padx=5, sticky="w")

    labelCategoria = Label(frmForm, text="Categoria")
    labelCategoria.config(font=('Arial', 12, 'bold'))
    labelCategoria.grid(column=4, row=0, pady=5, padx=5, sticky="w")

    # Entry del Frame frmForm
    entryCodigo = Entry(frmForm, textvariable=codigo)
    entryCodigo.grid(column=0, row=1, pady=5, padx=5)

    entryNombre = Entry(frmForm, textvariable=nombre)
    entryNombre.grid(column=1, row=1, pady=5, padx=5)

    entryAutor = Entry(frmForm, textvariable=autor)
    entryAutor.grid(column=2, row=1, pady=5, padx=5)

    entryStock = Entry(frmForm, textvariable=stock)
    entryStock.grid(column=3, row=1, pady=5, padx=5)

    # Instancia de la clase Categoria
    c = Categoria()
    # Lista de generos para el comboBoxCategoria
    lista = c.listarCategorias()

    # Combobox del Frame frmForm
    comboBoxCategoria = ttk.Combobox(
        frmForm, values=lista, textvariable=categoria)
    comboBoxCategoria.grid(column=4, row=1, pady=5)

    # Botones del Frame frmForm
    botonNuevo = Button(frmForm, text="Nuevo Registro", command=habilitar)
    botonNuevo.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                      bg='#158645', cursor='hand2', activebackground='#35BD6F')
    botonNuevo.grid(column=6, row=0, sticky="w", pady=2, padx=5)

    botonRegistrar = Button(frmForm, text="Registrar", command=registrar)
    botonRegistrar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                          bg='#1658A2', cursor='hand2', activebackground='#3586DF')
    botonRegistrar.grid(column=6, row=1, sticky="w", pady=2, padx=5)

    botonCancelar = Button(frmForm, text="Cancelar", command=desactivar)
    botonCancelar.config(font=('Arial', 8, 'bold'), fg='#DAD5D6',
                         bg='#BD152E', cursor='hand2', activebackground='#E15370')
    botonCancelar.grid(column=6, row=2, sticky="w", pady=2, padx=5)

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
        label="Arrendar Libros", command=bobContructor)

    createmenuPerfil = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Perfil", menu=createmenuPerfil)
    createmenuPerfil.add_command(label="Editar Perfil", command=bobContructor)
    createmenuPerfil.add_command(
        label="Libros Arrendados", command=bobContructor)
    createmenuPerfil.add_command(label="Ver Perfil", command=bobContructor)

    menubar.add_command(label="Configuracion", command=bobContructor)

    createmenuAyuda = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ayuda", menu=createmenuAyuda)
    createmenuAyuda.add_command(label="Soporte Tecnico", command=bobContructor)
    createmenuAyuda.add_command(
        label="Reportar Problema", command=bobContructor)
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
