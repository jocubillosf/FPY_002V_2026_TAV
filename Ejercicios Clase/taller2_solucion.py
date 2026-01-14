opcion = 1
edad = 0
usuario = ''
contrasena = ''
nota = 0
totalNota = 0
promedioNota = 0
opcionAnimal = 0
totalPuntos = 0
while opcion != 0:
    print("==TALLER 2==")
    print("1) Validación de edad")
    print("2) Usuario y Contraseña")
    print("3) Ingreso Notas")
    print("4) Quiz")
    print("0) Salir")
    print("Ingrese una opcion: ")
    opcion = int(input())
    
    if opcion == 1:
        print("Ingrese su edad: ")
        edad = int(input())
        if edad >= 18:
            print("Es mayor de edad")
        else: 
            print("Es menor de edad")
    elif opcion == 2:
        print("Ingrese Usuario: ")
        usuario = input()
        print("Ingrese Contraseña")
        contrasena = input()
        if usuario == 'pedro' and contrasena == '1234':
            print("Usuario validado")
        elif usuario == 'angel' and contrasena == 'a4s1':
            print("Usuario valido")
        else:
            print("Usuario o clave incorrecta")
    elif opcion == 3:
        for i in range (1,4):
            print("Ingrese nota ", i)
            nota = float(input())
            totalNota = totalNota + nota
        promedioNota = totalNota / 3
        if promedioNota >= 4:
            print("Aprobado")
        else:
            print("Reprobado")
    elif opcion == 4:
        print("¿Cual de los siguientes animales viven en el agua?")
        print("1) perro")
        print("2) cocodrilo")
        print("3) conejo")
        print("4) tiburón")
        print("Ingrese la opcion: ")
        opcionAnimal = int(input())
        if opcionAnimal == 4:
            totalPuntos = totalPuntos + 1
        elif opcionAnimal == 2:
            totalPuntos = totalPuntos + 0.5
        elif opcionAnimal == 1:
            totalPuntos = totalPuntos + 0
        elif opcionAnimal == 4:
            totalPuntos = totalPuntos + 0
        else:
            print("Ingrese opción valida")
