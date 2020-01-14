import sys
import os


print('''
Bienvenido a la calculadora python usa pycalcu.py -opciones [numero]
''')

print('1-dividir')
print('2-restar')
print('3-sumar')
print('4-multiplicar')

print('------------------------------------')
calculadora = input("calculadora: ")



print('------------------------------------')


if calculadora == "":
  print('No has seleccionado ninguna opcion')
  os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)



else:
  numero1 = int(input("Primer numero: "))
  numero2 = int(input("segundo numero: "))

if calculadora == "1": 
  print('========================')
  print('Dividicion!!')
  print('========================')

  resultado = str(numero1 / numero2)

if calculadora == "2": 
  print('========================')
  print('Resta!!')
  print('========================')
  resultado = str(numero1 - numero2)

if calculadora == "3": 
  print('========================')
  print('Suma!!')
  print('========================')
  resultado = str(numero1 + numero2)

if calculadora == "4": 
  print('========================')
  print('Multiplicacion!!')
  print('========================')
  resultado = str(numero1 * numero2)

print('Resultado es: ' + resultado)