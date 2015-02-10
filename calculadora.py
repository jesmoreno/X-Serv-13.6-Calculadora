#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

operadores = ['+', '-' , 'x', '/']

try:
    funcion = sys.argv[1]
    parametro1 = int(sys.argv[2]) 
    parametro2 = int(sys.argv[3]) 
except:
    print "Para multiplicar usar x"
    raise SystemExit

if funcion == operadores[0]:
    print str(parametro1) + '+' + str(parametro2) + ' = ' + str(parametro1 + parametro2)
elif funcion == operadores[1]:
    print str(parametro1) + '-' + str(parametro2) + ' = ' + str(parametro1 - parametro2)
elif funcion == operadores[2]:
    print str(parametro1) + '*' + str(parametro2) + ' = ' + str(parametro1 * parametro2)
elif funcion == operadores[3]:
    print str(parametro1) + '/' + str(parametro2) + ' = ' + str(parametro1 / parametro2)
else:
    print "Para ejecutarlo introducir : python calculadora.py función parametro1 parametro2"
    print "Solo acepta funciones : + , - , x , /"
        
