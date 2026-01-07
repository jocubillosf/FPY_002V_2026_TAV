#VARIABLES
edad = 0

print("==Validador de Edad==")
print("Ingrese su edad:")
edad = int(input())
##Operadores matemáticos >, <, >=, <=, !=
##Operadores lógicos or y and
## 1-10 años Niños
## 11- 17 años Adolecentes
## 18- 60 años Adultos
## 60 años o más Adultos Mayores
if edad >= 1 and edad <= 10:
    print("Es un niño")
else:
    print("Es menor de edad")
