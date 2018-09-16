import math
import sys

#Definido o calculo para a funcao
def f_x(x, func_escolhida):
    if func_escolhida == 1:
        resultado = x**3-(9*x)+5
        return resultado
    elif func_escolhida == 2:
        resultado = x**3-(9*x)+3
        return resultado
    elif func_escolhida == 3:
        resultado = math.exp(x)-3*x
        return resultado
    elif func_escolhida == 4:
        resultado = (2.75*x**3)+(18*x**2)-(21*x)-12
        return resultado
    else:
        print("Opcao Invalida")
        sys.exit(1)


#Definindo a derivada para a funcao tangente
def f_linha_x(x, func_escolhida):
    if func_escolhida == 1:
        resultado = 3*x**2-9
        return resultado
    elif func_escolhida == 2:
        resultado = 3*x**2-9
        return resultado
    elif func_escolhida == 3:
        resultado = math.exp(x)-3
        return resultado
    elif func_escolhida == 4:
        resultado = (8.25 *x**2)+(36*x)-21
        return resultado
    else:
        print("Opcao Invalida")
        sys.exit(1) 


#Metodo da Tangente (Newton Raphson)
def tangente_prec(x_0, prec, func_escolhida):
    if (abs(f_x(x_0, func_escolhida)) < prec):
        x_linha = x_0
    else:
        print ("Iteracao 0:")
        print ("x_linha: %f" %x_0)
        print ("f_barra_x: %f" %f_x(x_0, func_escolhida))
        k=1
        while True:
            x_1 = x_0 - (f_x(x_0, func_escolhida)/f_linha_x(x_0, func_escolhida))
            print ("Iteracao %d:" %k)
            print ("x_linha: %f" %x_1)
            print ("f_barra_x*: %f" %f_x(x_1, func_escolhida))
            if ((abs(f_x(x_1, func_escolhida)) < prec) or (abs(x_1 - x_0) < prec)):
                x_linha = x_1
                break
            else: 
                x_0 = x_1
            k = k +1
    return x_linha

#Metodo da Tangente (iteracoes)
def tangente_iteracoes(x_0, iteracoes, func_escolhida):
    print ("Iteracao 0:")
    print ("x_linha: %f" %x_0)
    print ("f_barra_x: %f" %f_x(x_0, func_escolhida))
    k=1
    while k <= iteracoes:
        x_1 = x_0 - (f_x(x_0, func_escolhida)/f_linha_x(x_0, func_escolhida))
        print ("Iteracao %d:" %k)
        print ("x_linha: %f" %x_1)
        print ("f_barra_x*: %f" %f_x(x_1, func_escolhida))
        x_0 = x_1
        k = k +1
    return x_1


#Metodo da Secante
def secante_prec(x_0, x_1, prec, func_escolhida):
    if (abs(f_x(x_0, func_escolhida)) < prec):
        x = x_0
    else:
        print ("Iteracao 0:")
        print ("x_0: %f" %x_0)
        print ("x_1: %f" %x_1)
        print ("f_barra_x: %f" %f_x(x_0, func_escolhida))
        if ((abs(f_x(x_1, func_escolhida)) < prec) or (abs(x_1 - x_0) < prec)):
            x = x_1
        else:
            k = 1
            while True:
                x_2 = x_1 - f_x(x_1, func_escolhida)*((x_1 - x_0)/(f_x(x_1, func_escolhida)-f_x(x_0, func_escolhida)))
                aux = x_2 - x_1
                print ("Iteracao %d:" %k)
                print ("x_0: %f" %x_0)
                print ("x_1: %f" %x_1)
                print ("f_x_2: %f" %f_x(x_2, func_escolhida))
                print ("x_2-x - x_1: %f" %aux)
                if ((abs(f_x(x_2, func_escolhida)) < prec) or (abs(aux) < prec)):
                    x = x_2
                    break
                else:
                    x_0 = x_1
                    x_1 = x_2

                k = k+1
    return x

#Metodo da secante (iteracoes)
def secante_iteracoes(x_0, x_1, iteracoes, func_escolhida):
    print ("Iteracao 0:")
    print ("x_0: %f" %x_0)
    print ("x_1: %f" %x_1)
    print ("f_barra_x: %f" %f_x(x_0, func_escolhida))
    k = 1
    while k <=iteracoes:
        x_2 = x_1 - f_x(x_1, func_escolhida)*((x_1 - x_0)/(f_x(x_1, func_escolhida)-f_x(x_0, func_escolhida)))
        aux = x_2 - x_1
        print ("Iteracao %d:" %k)
        print ("x_0: %f" %x_0)
        print ("x_1: %f" %x_1)
        print ("f_x_2: %f" %f_x(x_2, func_escolhida))
        print ("x_2-x - x_1: %f" %aux)
        x_0 = x_1
        x_1 = x_2
        k = k+1
    return x_2



def menu():
    print("Bem-vindo(a) a calculadora de Bisseccao e Falsa Posicao!\nOpcoes:")
    print("1) Secante (Precisao)")
    print("2) Secante (Iteracoes)")
    print("3) Tangente (Precisao)")
    print("4) Tangente (Iteracoes)")
    print("5) Sair")
    escolha = int(input("O que voce deseja fazer? (Digite o numero com a opcao desejada)\n"))

    if escolha == 1:
        x_0 = float(input("Digite o valor de x0:\n"))
        x_1 = float(input("Digite o valor de x1:\n"))
        prec = float(input("Digite a precisao:\n"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        func_escolhida = int (input("Digite a funcao escolhida:\n")) 
        secante_prec(x_0, x_1, prec, func_escolhida)     
        
    elif escolha == 2:
        x_0 = float(input("Digite o valor inicial de x0:\n"))
        x_1 = float(input("Digite o valor final de x1:\n"))
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        func_escolhida = int (input("Digite a funcao escolhida:\n"))
        secante_iteracoes(x_0, x_1, iteracoes, func_escolhida)

    elif escolha == 3:
        x_0 = float(input("Digite o valor de x0:\n"))
        prec = float (input("Digite a precisao\n"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        func_escolhida = int (input("Digite a funcao escolhida:\n"))
        tangente_prec(x_0, prec, func_escolhida)
        
    elif escolha == 4:
        x_0 = float(input("Digite o valor inicial de x0:\n"))
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        func_escolhida = int (input("Digite a funcao escolhida:\n"))
        tangente_iteracoes(x_0, iteracoes, func_escolhida)

    elif escolha == 5:
        sys.exit(0)
    else:
        print("Opcao Invalida")

menu()

