# Enunciado : Realizar un programa en Python que me
#permita calcular el promedio final de acuerdo a la formula
#de Idat


# Entrada : Input
print('---------------ENTRADA--------------------')

print('Buenos dias!')
print('Por favor Ingresa tu Nombre Completo:')
alumno=input('- ')
eco1= float(input('Por favor ingresa tu Nota 1    : '))
eco2= float(input('Por favor ingresa tu Nota 2    : '))
eco3= float(input('Por favor ingresa tu Nota 3    : '))
ef  = float(input('Por favor ingresa tu Nota Final: '))

# Proceso : Process (Lo que vas a programar)
nota1=eco1*0.04
nota2=eco2*0.12
nota3=eco3*0.24
ev=ef*0.60

promedio=nota1+nota2+nota3+ev


# Salida : Output
print('---------------SALIDA--------------------')

print('El % que aplica de tu Nota1 es de 4%  : ',round(nota1,2))
print('El % que aplica de tu Nota2 es de 12% : ',round(nota2,2))
print('El % que aplica de tu Nota3 es de 24% : ',round(nota3,2))
print('El % que aplica de tu Eva.F. es de 60%: ',round(ev,2))
print('El Promedio Final de tu Curso es de   : ',round (promedio,2))
