

def validar_opcion():
    while True:
        try:
            opcion = int(input("Escoga una opción del Menú (1 al 4): "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! Escoga una opción correcta")
        except:
            print("ERROR! La opcion debe ser un número entero")


def validar_nombre_dueño():
    while True:
        nombre = input("Ingrese nombre dueño: ")
        if len(nombre) >= 3 and nombre.isalpha():
            #break
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")


def validar_dias(): 
    while True:
        try:
            dias = int(input("Ingrese días a hospedar: "))
            if dias >= 1:
                return dias
            else:
                print("ERROR! LOS DÍAS DEBEN SER 1 O MÁS!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre mascota: ")
        if len(nombre) >= 3 and nombre.isalpha():
            #break
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")


def validar_habitacion():
    
    while True:
        try:
            habitacion = int(input("selec cione su habitación: "))
            if habitacion >= 1 and habitacion <=10:
                return habitacion
            else:
                print("ERROR! La habitación debe ser entre 1 y 10!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
