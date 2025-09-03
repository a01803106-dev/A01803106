print("Hello World")

donas = int(input("¿Cuántas donitas tienes? "))
docenas = donas // 12
print("Con", donas, "donas puedes hacer", docenas, "docenas!")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
residuo = num1 % num2
print(num1, "dividido entre", num2, "tiene un residuo de", residuo, "!")

segundos = int(input("Ingresa un numero de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(segundos, "segundos son", horas, "horas,", minutos, "minutos y", segundos_restantes, "segundos")
