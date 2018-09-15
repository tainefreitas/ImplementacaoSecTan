import math
import sys

#Definido o calculo para a funcao teste
def f_x(x):
    resultado = x**3-(9*x)+3
    return resultado


def f_linha_x(x):
    resultado = 3*x**2-9
    return resultado

#Metodo da Tangente (Newton Raphson)
def tangente_prec(x_0, prec):
    if (abs(f_x(x_0)) < prec):
        x_linha = x_0
    else:
        print ("Iteracao 0:")
        print ("x_linha: %f" %x_0)
        print ("f_barra_x: %f" %f_x(x_0))
        k=1
        while True:
            x_1 = x_0 - (f_x(x_0)/f_linha_x(x_0))
            print ("Iteracao %d:" %k)
            print ("x_linha: %f" %x_1)
            print ("f_barra_x*: %f" %f_x(x_1))
            print("Obs: por conta das casas decimais, o resultado difere dos slides, mas esta correto.")
            if ((abs(f_x(x_1)) < prec) or (abs(x_1 - x_0) < prec)):
                x_linha = x_1
                break
            else: 
                x_0 = x_1
            k = k +1
    return x_linha

#Metodo da Secante (perguntar pra professora a equacao do x_2)
def secante_prec(x_0, x_1, prec):
    if (abs(f_x(x_0)) < prec):
        x = x_0
    else:
        print ("Iteracao 0:")
        print ("x_linha: %f" %x_0)
        print ("f_barra_x: %f" %f_x(x_0))
        if ((abs(f_x(x_1) < prec)) or (abs(x_1 - x_0) < prec)):
            x = x_1
        else:
            k = 1
            while True:
                x_2 = x_1 - f_x(x_1)*((x_1 - x_0)/(f_x(x_1)-f_x(x_0)))
                print ("Iteracao %d:" %k)
                print ("x_linha: %f" %x_2)
                print ("f_barra_x*: %f" %f_x(x_2))
                print("Obs: por conta das casas decimais, o resultado difere dos slides, mas esta correto.")

                if ((abs(f_x(x_2)) < prec) or (abs(x_2 - x_1) < prec)):
                    x = x_2
                    break
                else:
                    x_0 = x_1
                    x_1 = x_2

                k = k+1
    return x

tangente_prec(0.75, 0.01)