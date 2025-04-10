#ex1-
#corre os 200 numeros
for i in range(1,201):
    #valida os numeros pares
    if(i%2==0):
        print(i)

#ex2-
#entrada da quantidade de alunos
alunos=int(input())
#declaração da variavel de controle 
quant_alunos_apv=0
#consultando e validando nota de todos os alunos
for i in range(alunos):
    #entrada da nota de um alunos
    nota=float(input())
    #verifica se o aluno é maior que a média
    if(nota>=6.0):
        quant_alunos_apv+=1
#saida da quantidade de alunos com nota para serem aprovados
print(quant_alunos_apv)

#ex3-
#leitura de um numero inteiro
num=int(input())
primo=True
i=2
#verifica todos os numeros de 1 até o valor do numero
while (i<=num):
    if(i==num):
        i=num
    elif (num%i==0):
        primo=False
    i+=1
    
#com base nos comandos anteriores valida se num é primo ou nao
if(primo==True):
    print("Primo")
else:
    print("Não é primo")

#ex4-
# Uma loja de discos anota diariamente a quantidade de discos vendidos. Dados um inteiro n que representa a quantidade de dias do intervalo 
# e a quantidade de discos vendidos no período, determine em que dia desse período ocorreu a maior venda e qual foi a quantidade de discos 
# vendida nesse dia. Em caso de empate, considere o primeiro dia de maior venda.
# Entrada:  a entrada é composta de um inteiro n, que indica o número de dias do intervalo. em seguida são lidos n números inteiros indicando a quantidade 
# de discos vendidos em cada um dos dias.
# Saída:  saída consiste em dois inteiros representando o o dia do intervalo que ocorreu a maior venda e a quantidade de discos vendidos neste dia

#leitura da quantidade de dias
quant_dias=int(input())

#declaração das variaveis que vao armazenar o valor de maior quantidade e o dia que esse fato ocorre
maior_quant=-1
dia_maior_quant=0
#declaração de variavel que armazenara que dia é
dia=0
#looping para receber os dados dos dias
for i in range(quant_dias):
    #leitura da quantidade de venda
    quant_vendida=int(input())
    #registro do dia em que foi vendido a quantidade de venda da variavel quant_vendida
    dia+=1
    #compara o maior numero armazenado com o numero recem lido e armazena o dia, caso o numero recem lido seja maior que o anterior
    if(maior_quant<quant_vendida):
        maior_quant=quant_vendida
        dia_maior_quant=dia
    
#saida do dia de maior quantidade e o valor
print(dia_maior_quant,maior_quant)

# ex5-
# Projete e implemente um programa em C que leia vários valores reais, cada um indicando o raio de uma dada circunferência 
# e para cada valor de raio calcule e imprima o perímetro e a área dessa circunferência. Obs.: Utilize a constante math.pi e não esqueça do import.

# Entrada: A primeira informação lida é um número inteiro n > 0 que representa o número de vezes que o programa será executado, 
# seguido de n números reais indicando o raio de uma circunferência.

# Saída: A saída consiste em imprimi# r para cada número real o valor o perímetro e a área da circunferência com duas casas decimais após a vírgula.


#import da biblioteca math de python
import math
#entrada de numero de raios que seram lidos
quant_raios=int(input())

#leitura do raio e calculo de seu perimetro e sua area
for i in range(quant_raios):
    #leitura raio
    raio=float(input())
    #calculo perimetro
    perimetro=2*math.pi*raio
    #calculo area
    area=math.pi*raio**2
    #saida do perimetro e area com 2 casas decimais
    print(f"{perimetro:.2f} {area:.2f}")

#ex6-
# O fatorial de um número é o produto dele pelos seus antecessores maiores que 0. 
# Faça um programa que leia um número inteiro e calcule o fatorial de n.

# Entrada: a entrada é composta por um inteiro 1 <= n  <= 15 .

# Saída:  a saída do programa deverá imprimir o fatorial de n.

#entrada de um numero para calculo do fatorial
num=int(input())
#declaração da variavel de armazenamento do fatorial
fat=1
#fazer o calculo apartir da multiplicação dos numeros até chegar no numero que se deseja o fatorial
for i in range(1,num+1):
    #calculo do fatorial
    fat=fat*i
#saida do fatorial
print(fat)