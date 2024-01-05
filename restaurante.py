from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    # Check para comida
    x = 0
    for c in cuadros_comida:
        if variable_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    # Check para bebida
    x = 0
    for b in cuadros_bebida:
        if variable_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    # Check para postres
    x = 0
    for p in cuadros_postres:
        if variable_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 63)
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 75 + '\n')
    texto_recibo.insert(END, f'Costo comidas: \t\t\t ${var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo bebidas: \t\t\t ${var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo postres: \t\t\t ${var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'subtotal: \t\t\t ${var_subtotal.get()}\n')
    texto_recibo.insert(END, f'impuestos: \t\t\t ${var_impuestos.get()}\n')
    texto_recibo.insert(END, f'total: \t\t\t ${var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63)
    texto_recibo.insert(END, f'Lo esperamos pronto!')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

# Iniciando tkinter
aplicacion = Tk()

# Ajustando tamaño de pantalla
aplicacion.geometry('1200x720+0+0')

# Evitar maximizar
aplicacion.resizable(0, 0)

# Titulo en ventana
aplicacion.title('Mi_Proyecto')

# Color de fondo
aplicacion.config(bg='#283618')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
    # Titulo
etiqueta_titulo = Label(panel_superior, 
                        text='Mi_proyecto', 
                        fg='azure4', 
                        font=('Dosis', 50), 
                        bg='burlywood', 
                        width=25)
etiqueta_titulo.grid(row=0, column=0)
# ---> Fin panel superior <---

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=SUNKEN, padx=110, bg="azure4")
panel_costos.pack(side=BOTTOM)
# ---> Fin panel costos <---

# Panel comida
panel_comidas = LabelFrame(panel_izquierdo, 
                            text='Comidas', 
                            font=('Dosis', 15, 'bold'), 
                            bd=1, 
                            relief=SUNKEN, 
                            fg='#606c38')
panel_comidas.pack(side=LEFT)
# ---> Fin panel comida <---

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, 
                            text='Bebidas', 
                            font=('Dosis', 15, 'bold'), 
                            bd=1, 
                            relief=SUNKEN, 
                            fg='#606c38')
panel_bebidas.pack(side=LEFT)
# ---> Fin panel bebidas <---

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, 
                            text='Postres', 
                            font=('Dosis', 15, 'bold'), 
                            bd=1, 
                            relief=SUNKEN, 
                            fg='#606c38')
panel_postres.pack(side=LEFT)
# ---> Fin panel comida <---
# ---> Fin panel izquierdo <---

# Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_derecho.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=SUNKEN)
panel_calculadora.pack()
# ---> Fin panel calculadora <---

# Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=SUNKEN)
panel_recibo.pack()
# ---> Fin panel recibo <---

# Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=SUNKEN)
panel_botones.pack()
# ---> Fin panel botones <---
# ---> Fin panel derecho <---

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'pizza', 'hamburguesas', 'ramen', 'gohan']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'flan', 'mousse', 'torta', 'brownies', 'milkshake', 'donas']
# ---> Fin lista de productos <---

# Loop para crear checks comida
variable_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # Creacion de check
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                        text=comida.title(), 
                        font=('Dosis', 15, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variable_comida[contador],
                        command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    # Cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, 
                                    font=('Dosis', 15, 'bold'), 
                                    bd=1,
                                    width=10,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador],
                                    justify=CENTER)
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1
# ---> Fin loop <---

# Loop para crear checks bebidas
variable_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variable_bebida.append('')
    variable_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                        text=bebida.title(), 
                        font=('Dosis', 15, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variable_bebida[contador],
                        command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    # Cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, 
                                    font=('Dosis', 15, 'bold'), 
                                    bd=1,
                                    width=10,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador],
                                    justify=CENTER)
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1
# ---> Fin loop <---

# Loop para crear checks postres
variable_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    variable_postres.append('')
    variable_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, 
                        text=postres.title(), 
                        font=('Dosis', 15, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variable_postres[contador],
                        command=revisar_check)
    postres.grid(row=contador, column=0, sticky=W)

    # Cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, 
                                    font=('Dosis', 18, 'bold'), 
                                    bd=2,
                                    width=10,
                                    state=DISABLED,
                                    textvariable=texto_postres[contador],
                                    justify=CENTER)
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1
# ---> Fin loop <---
    
# Etiqueta de costos y campos
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

etiqueta_costo_comida = Label(panel_costos,
                            text='Costo Comida',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                            text='Costo Bebida',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                            text='Costo Postres',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                        text='Subtotal',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=8,
                    state='readonly',
                    textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                        text='Impuestos',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=8,
                    state='readonly',
                    textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                        text='Total',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=8,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)
# ---> Fin etiqueta de costos y campos <---

# Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
contador_columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                text=boton.title(),
                font=('Dosis', 12, 'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=9)
    
    botones_creados.append(boton)
    boton.grid(row=0, column=contador_columnas)
    contador_columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
# --> Fin botones <---
    
# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=11)
texto_recibo.grid(row=0, column=0)
# ---> Fin area de recibo <---

# calculadora
visor_calculadora = Entry(panel_calculadora,
                        font=('Dosis', 16, 'bold'),
                        width=32,
                        bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)
# ---> Fin calculadora <---

# Botonos de calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                text=boton.title(),
                fg='white',
                bg='azure4',
                bd=1,
                width=9,
                font='bold')
    
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))
# ---> Fin de botones de calculadora <---

# evitando que la pantalla se cierre
aplicacion.mainloop()