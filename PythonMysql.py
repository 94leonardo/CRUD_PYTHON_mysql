import tkinter as tk

# importar los modulos restantes  de tkinter

from tkinter import *

from tkinter import ttk, messagebox

from Clientes import *
from Conexion import *


class FormularioClientes:

    global base, texBoxId, texBoxNombres, texBoxApellidos, combo, groupBox, tree

    base = texBoxId = texBoxNombres = texBoxApellidos = combo = groupBox = tree = None


@staticmethod
def Formulario():

    global texBoxId, texBoxNombres, texBoxApellidos, combo, base, groupBox, tree

    try:
        base = Tk()
        base.geometry("1200x170")
        base.title("Formulario Python")

        groupBox = LabelFrame(
            base, text="Datos Personales", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        LabelId = Label(groupBox, text="Id:", width=13, font=("arial", 12))
        LabelId.grid(row=0, column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=0, column=1)

        LabelNombres = Label(groupBox, text="Nombres:",
                             width=13, font=("arial", 12))
        LabelNombres.grid(row=1, column=0)
        texBoxNombres = Entry(groupBox)
        texBoxNombres.grid(row=1, column=1)

        LabelApellido = Label(groupBox, text="Apellidos:",
                              width=13, font=("arial", 12))
        LabelApellido.grid(row=2, column=0)
        texBoxApellidos = Entry(groupBox)
        texBoxApellidos.grid(row=2, column=1)

        LabelSexo = Label(groupBox, text="Sexo:", width=13, font=("arial", 12))
        LabelSexo.grid(row=3,  column=0)
        seleccionSexo = tk.StringVar()
        combo = ttk.Combobox(
            groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
        combo.grid(row=3, column=1)
        seleccionSexo.set("Masculino")

        Button(groupBox, text="Guardar", width=10,
               command=guardarRegistros).grid(row=4, column=0)
        Button(groupBox, text="Modificar", command=modificarRegistros,
               width=10).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", command=elimiarRegistro,
               width=10).grid(row=4, column=2)

        groupBox = LabelFrame(
            base, text="Lista del personal", padx=5, pady=5,)
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        # Crear un treeviw

        # Configurar las columnas

        tree = ttk.Treeview(groupBox, columns=(
            "Id", "Nombres", "Apellidos", "Sexo"), show='headings', heigh=5,)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id")

        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombres")

        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Apellidos")

        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Sexo")

        # Agregar los datos a la tabla
        # mostra la tabla

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        # ejecutar la funcion al hacer click y mostrar el resultado en los Entry

        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

        tree.pack()

        base.mainloop()

    except ValueError as error:
        print(f"Error al mostrar la interfaz,error: {error}")


@staticmethod
def guardarRegistros():

    global texBoxNombres, texBoxApellidos, combo, groupBox

    try:
        # verificar si los widgets (botosnes) estan inicializados

        if texBoxNombres is None or texBoxApellidos is None or combo is None:
            print("los Widgets no estan inicialisados")
            return
        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()

        CClientes.ingresarClientes(nombres, apellidos, sexo)
        messagebox.showinfo("Informacion", "Los datos estan ingresados")

        actualizarTreeView()

        # limpiar los datos de los campos

        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except ValueError as error:
        print(f"Error al ingresar los datos: {error}")


def actualizarTreeView():

    global tree

    try:
        # Borrar todo los elementos actuales de treeView
        tree.delete(*tree.get_children())

        # obtener los nuevos datos que deseamos mostrar

        datos = CClientes.mostrarClientes()

        # Insaertar los nuevos datos en treeView

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

    except ValueError as error:
        print(f"Error al actualizar tabla: {error}")


def seleccionarRegistro(evnto):
    try:
        # obatener el id del elemnto seleccionado

        itemSeleccionado = tree.focus()

        if itemSeleccionado:
            # Obtener valores por columnas
            values = tree.item(itemSeleccionado)['values']
            # Establecer los valores dels widgets Entry

            texBoxId.delete(0, END)
            texBoxId.insert(0, values[0])
            texBoxNombres.delete(0, END)
            texBoxNombres.insert(0, values[1])
            texBoxApellidos.delete(0, END)
            texBoxApellidos.insert(0, values[2])
            combo.set(values[3])

    except ValueError as error:
        print(f"Error al seleccionar el registro: {error}")


def modificarRegistros():

    global texBoxId, texBoxNombres, texBoxApellidos, combo, groupBox

    try:
        # verificar si los widgets (botosnes) estan inicializados

        if texBoxId is None or texBoxNombres is None or texBoxApellidos is None or combo is None:
            print("los Widgets no estan inicialisados")
            return
        idUsuarios = texBoxId.get()
        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()

        CClientes.modificarClientes(idUsuarios, nombres, apellidos, sexo)
        messagebox.showinfo("Informacion", "Los datos estan Actualizados")

        actualizarTreeView()

        # limpiar los datos de los campos
        texBoxId.delete(0, END)
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except ValueError as error:
        print(f"Error al Actualizar los datos: {error}")


def elimiarRegistro():

    global texBoxId, texBoxNombres, texBoxApellidos

    try:
        # verificar si los widgets (botosnes) estan inicializados

        if texBoxId is None:
            print("los Widgets no estan inicialisados")
            return
        idUsuarios = texBoxId.get()

        CClientes.EliminarClientes(idUsuarios)
        messagebox.showinfo("Informacion", "Los datos estan Eliminar")

        actualizarTreeView()

        # limpiar los datos de los campos
        texBoxId.delete(0, END)
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except ValueError as error:
        print(f"Error al Eliminar los datos: {error}")


Formulario()
