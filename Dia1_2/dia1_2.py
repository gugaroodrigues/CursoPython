
print('Hello ')


#tipos de variaveis primitivas

idade = 28 # Int nueros inteiros
peso = 80.4  # float numeros decimais
nome = 'Jose' # Str caracteres
ativo = True # bool  valores logicos
resultado = None # None ausência de valor

print(type(idade))
print(type(peso))
print(type(nome))
print(type(ativo))
print(type(resultado))

#Dia 2, calculos, exemplos de soma com python, Atibuição aumentada,
num1 = 10
num2 = 5

resultado = num1 + num2
print(num1)
print(num2)
print(resultado)

#Exemplo soma

alunos_presentes = 23
alunos_ausentes = 17
total_alunos = alunos_ausentes + alunos_presentes

print(total_alunos)

#atibuição aumentada

numero1 = 10
numero2 = 3
resultado1 = numero1 + numero2
print(resultado1)

pro1 = 10
pro1 += 3 # Operador de atribuição aumentada **= potencia  //divisão inteira
print(resultado1)

#funções basicas com numeros

nume = 3.6425


print(nume)
print(round(nume, 3))

print(pow(2,3))

print(max(1, 4, 9, 2, 17, 13))
print(min(1, 4, 9, 2, 17, 13))
print(sum([1, 4, 9, 2, 17, 13]))

#ordem dos operadores faz diferença

# Ordem dos operadoes
# 1 Parênteses ()
# 2 Exponenciação **
# 3 Multiplicação *
# 4 Divisão /
# 5 Divisão Inteira //
# 6 Modulo %
# 7 Adição +
# 8 Subtração -

resultado_op = 10 + 2 * 3 # 16
resultado_op2 = 10 + (2 * 3) #

#Modulo Math

import math

print(math.ceil(4.2))
print(math.floor(4.7))
print(math.pow(2,3))
print(math.sqrt(16))



