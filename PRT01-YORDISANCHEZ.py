
# Captura de numeros por teclado
numero1 = float(input("Escribir el primer numero: "))  
numero2 = float(input("Escribir el segundo numero: ")) 

# Declarando variables para que pueda calcular
N1elevado1 = numero1 ** 2 #
N1elevado2 = numero2 ** 2 #
sresultado = N1elevado2 + N1elevado2 #
rresultado = "{:.4f}".format(sresultado ** (1/2)) # Utilizamos "4f" para que podamos decidir la cantidad de decimales que queremos mostrar luego del punto.

# Asignamos la formula y imprimos el resultado final de la operacion.
print ("√(" + str(numero1) + "²" + " + " + str(numero2) + ")²" +" = " + "√("+ str(N1elevado1) + " + " + str(N1elevado2)  + ") = " + "√("+ str(sresultado) + ") = " + str(rresultado)   )