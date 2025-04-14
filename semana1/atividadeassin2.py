#EX1
#  (OBI 2021) Atletas conseguem resultados cada vez melhores! O recorde mundial de uma determinada modalidade esportiva é o melhor resultado conseguido por um 
# atleta nessa modalidade, em competições oficiais. Competições oficiais incluem campeonatos mundiais, como os campeonatos mundiais de ginástica, 
# atletismo ou natação, e também as Olimpíadas.

# Como as Olimpíadas acontecem a cada quatro anos e competições oficiais acontecem todos os anos, é possível que o melhor resultado obtido em Olimpíadas em uma dada 
# modalidade seja um resultado pior do que o recorde mundial para aquela modalidade. Por isso, nas provas das Olimpíadas são sempre mencionados dois recordes: 
# o recorde olímpico (melhor resultado que já foi obtido em Olimpíadas) e o recorde mundial (melhor resultado em qualquer competição oficial, incluindo as Olimpíadas).

# Nesta tarefa, dados o resultado de uma prova nas Olimpíadas e os recordes mundial e olímpico para essa prova, sua tarefa é determinar se o resultado é um 
# novo recorde mundial e/ou um novo recorde olímpico.

# Entrada: a entrada é composta por três linhas. A primeira linha é um inteiro R, o melhor resultado obtido por um atleta numa prova das Olimpíadas. 
# A segunda linha é um inteiro M, o recorde mundial para essa prova. A terceira linha é um inteiro L, o recorde olímpico para essa prova.
#  Para as provas desta tarefa, ****************quanto menor o valor melhor o resultado*****************.

# Saída: seu programa deve produzir duas linhas. A primeira linha deve ser RM se o resultado é um recorde mundial, ou * (asterisco) caso contrário.
# A segunda linha deve ser RO se o resultado é um recorde olímpico, ou * (asterisco) caso contrário. 


#entrada de 3 numero inteiros
mlhresultoplim=int(input())
recordmund=int(input())
recordolim=int(input())

#compara os valores do melhor resultado de um atleta e do record mundial
if(mlhresultoplim<recordmund):
    print("RM")
else:
    print("*")

#compara os valores do melhor resultado de um atleta e do record olimpico
if(mlhresultoplim<recordolim):
    print("RO")
else:
    print("*")

#EX 2
# (OBI 2019) Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a soma das idades dos seus três filhos é igual à idade dela. 
# Neste problema, dada a idade de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a idade do filho mais velho.

# Por exemplo, se sabemos que dona Mônica tem 52 anos e as idades conhecidas de dois dos filhos são 14 e 18 anos, então a idade do outro filho, 
# que não era conhecida, tem que ser 20 anos, pois a soma das três idades tem que ser 52. Portanto, a idade do filho mais velho é 20. Em mais um exemplo, 
# se dona Mônica tem 47 anos e as idades de dois dos filhos são 21 e 9 anos, então o outro filho tem que ter 17 anos e, portanto, a idade do filho mais velho é 21.

# Entrada: a primeira linha da entrada contém um inteiro M representando a idade de dona Mônica. A segunda linha da entrada contém um inteiro A 
# representando a idade de um dos filhos. A terceira linha da entrada contém um inteiro B representando a idade de outro filho.

# Saída: seu programa deve imprimir uma linha, contendo um número inteiro, representando a idade do filho mais velho de dona Mônica.


#entrada da idade da mae e do dois filhos
iddmae=int(input())
iddfilhoA=int(input())
iddfilhoB=int(input())

#declaração var filho C
iddfilhoC=0

#calculo da idade do filho C
iddfilhoC=iddmae-(iddfilhoA+iddfilhoB)

#verificação de qual irmao é mais velho co base em if, elif e else.
#condição de filho a mais velho
if iddfilhoA>iddfilhoB and iddfilhoA>iddfilhoC:
    print(iddfilhoA)

#condição filho b mais velho
elif(iddfilhoB>iddfilhoA and iddfilhoB>iddfilhoC):
    print(iddfilhoB)

#por eliminação, filho c mais velho
else:
    print(iddfilhoC)


# EX3

# (OBI 2020) Um aplicativo de celular está sendo desenvolvido para, a partir da foto de um prato contendo uma refeição, estimar a quantidade de calorias da refeição. 
# O algoritmo de inteligência artificial (IA) utilizado no aplicativo produz três números inteiros, E1, E2 e E3. 
# E1 é a quantidade mínima de calorias estimada e E2 a quantidade máxima de calorias estimada para a refeição da fotografia. 
# E3 só tem significado se a diferença entre as quantidades estimadas mínima e máxima são maiores do que um valor pré-definido X; nesse caso, 
# E3 é a quantidade de calorias estimada por um método alternativo. Depois de vários testes, os desenvolvedores do aplicativo determinaram 
# que os melhores resultados são obtidos usando as estimativas produzidas pelo algoritmo de IA da seguinte forma:

# se a diferença entre E1 e E2 for menor ou igual ao valor de X, o aplicativo deve mostrar ao usuário o valor de E2 como o número de calorias;
# se a diferença entre E1 e E2 for maior do que o valor de X, o aplicativo deve mostrar ao usuário o valor de E3 como o número de calorias;
# Dados o valor de X e as três estimativas produzidas pelo algoritmo de IA, escreva um programa que determine o resultado que deve ser mostrado para o usuário.

# Entrada: a primeira linha da entrada contém um inteiro, o valor de E1. A segunda linha contém um inteiro, o valor de E2. 
# A terceira linha contém um inteiro, o valor de E3. A quarta linha contém um inteiro, o valor de X.

# Saída: seu programa deve produzir uma única linha, contendo um único inteiro, o resultado que deve ser mostrado para o usuário do aplicativo.


#entrada de 4 numeros inteiros
qttminesti=int(input())
qttmaxesti=int(input())
qttpormetalt=int(input())
x=int(input())

#saida por condições em if e else
#verifica se a subtração da um numero positivo e é menor ou igual a x
if (qttminesti-qttmaxesti)>=0 and ((qttminesti-qttmaxesti)<=x): 
    print(qttmaxesti)
#verifica se a subtração da um numero negativo e se for o multiplica por menos 1 e depois compara se é menor ou igual a x
elif((qttminesti-qttmaxesti)<=0) and ((qttminesti-qttmaxesti)*(-1)<=x):
    print(qttmaxesti)
#saida caso nao for nenhuma das duas condições
else:
    print(qttpormetalt)


#EX4-com erro
#  (OBI 2020) Dona Lesma é esportista e aventureira e definiu como objetivo deste verão alcançar o topo do muro do jardim em que vive. 
# A cada dia, valente e metodicamente ela sobe exatamente uma certa distância (sempre a mesma a cada dia).
#  Mas a cada noite enquanto dorme Dona Lesma escorrega para baixo uma outra distância (sempre a mesma a cada noite)...

# Dadas a altura do muro, a distância que ela sobe a cada dia e a distância que ela desce a cada noite, 
# ajude Dona Lesma a calcular quantos dias ela levará para chegar ao topo do muro.

# Entrada: a primeira linha contém um inteiro A, a altura do muro. A segunda linha contém um inteiro S, d
# istância que Dona Lesma sobe a cada dia. A terceira linha contém um inteiro D, a distância que Dona Lesma escorrega para baixo a cada noite.

# Saída: seu programa deve produzir uma única linha, contendo um único inteiro, 
# o número de dias que Dona Lesma demorará para chegar ao topo do muro.


#entrada de 3 numeros inteiros
altmuro=int(input())
distsub=int(input())
distdesc=int(input())

#declaração de variaveis necessarias
alttotal=0
dia=0
saldodia=distsub-distdesc

#laço enquanto a altura do muro for menor que a altura alcançada
while (altmuro!=alttotal):  
    alttotal=alttotal+saldodia
    dia+=1

#saida da quantidade de dias
print(dia)

# EX5-

# Faça um programa que leia o número de termos, determine e mostre os valores de acordo com a série abaixo: 
# S = 2; 7; 3; 4; 21; 12; 8; 63; 48; 16; 189; 192; 32; 567; 768; 64; ...

# Entrada: a entrada consiste em um inteiro n > 3, que indica o número de termos da sequência a ser impresso.

# Saída: a saída deverá ser impressa em uma única linha, contendo os n termos da sequência.


#semente1->inicia no 2 e é mult por 2
#semente2->inicia no 7 e é mult por 3
#semente3->inicia no 3 e é mult por 4


#entrada de um numero int
n=int(input())

#declaração de var necessarias
s1=2
s2=7
s3=3
i=0

#retirando os 3 primeiros numeros que sao sementes
n=n-3

#saida dos 3 primeiros numeros da sequencia
print(s1,s2,s3,end=" ")

#laço de repetição enquanto i for menor que n
while i<n:
    #calcula o proximo termo da semente1
    s1*=2
    print(s1,end=" ")
    i+=1

    #verifica se ainda nao foi até o numero de termos e se nao for continua e calcula a semente 2
    if i<n:
        s2*=3
        print(s2,end=" ")
        i+=1
        
    #verifica se ainda nao foi até o numero de termos e se nao for continua e calcula a semente 3
    if i<n:
        s3*=4
        print(s3,end=" ")
        i+=1

# EX6-
# Faça um programa em Pyhton que imprima os 100 primeiros pares positivos utilizando a estrutura de repetição for.

for i in range(2,101):
    if i%2==0:
        print(i)
# EX7-


# EX 8
# Faça um programa que Imprima os 100 primeiros inteiros positivos, utilizando o laço while.

i=1
while i<101:
    print(i)
    i+=1

# EX9
# Faça um programa que leia dois inteiros n e m e, em seguida, leia n valores e determine quantos são maiores do que m e quantos são menores ou iguais a m.

# Entrada: dois inteiros n > 1 e m

# Saída: a saída consiste em dois inteiros, sendo que a primeira informação é a quantidade de 
# números maiores que m e a segunda informação é a quantidade de números menores ou iguais a m.

#leitura de 2 numeros inteiros n e m
n,m=input().split()

#transformação para numero inteiro
n=int(n)
m=int(m)

#declaração de variaveis importantes
num=0
maiorquem=0
menorquem=0

# laco de repetição para ler a quantidade n de valores
for i in range(n):
    num=int(input())

    # sistema if e else para ver se o numero é maior ou menor que m
    if num>m:
        maiorquem+=1
    else:
        menorquem+=1

# saida da quantidade de numeros maiores e menores ou iguais a m        
print(maiorquem,menorquem)






# EX14-terminar

# Faça um programa que leia o ano atual e a porcentagem de aumento anual a receber por um funcionário. Em seguida, calcule e mostre o salário atual de um funcionário, 
# sabendo-se o salário inicial de contratação, o ano da contratação.  Considere que ele recebe aumento no mês de janeiro de cada ano.

# Entrada:  a entrada é composta por duas linhas. A primeira linha contém um inteiro que corresponde ao ano em que se quer calcular o 
# reajuste e um número real que corresponde à porcentagem anual de reajuste. A segunda linha contém um inteiro que corresponde ao ano 
# de contratação do funcionário e um real s > 500.00, indicando o salário inicial do funcionário.

# Saída: a saída consiste em um real com duas casas decimais, representando o salário corrigido.

#leitura do ano atual e porcentagem de aumento anual
anoat,porcauanual=input().split()

#leitura do salario inicial e ano da contratação
salinicial,anocont=input().split()

#transformação dos dados
anoat=int(anoat)
porcauanual=float(porcauanual)
salinicial=float(salinicial)
anocont=int(anocont)






# EX15-
# Faça um programa que leia um inteiro n e imprima a Tabuada de n.

# Entrada: a sua entrada contém uma linha com um inteiro n > 1.

# Saída: a tabuada de n.

#entrada de um numero inteiro
num=int(input())

#declaração da variavel que vai armazenar a multiplicaçõa
mult=1

#laço de repetição para fazer a tabuada
for i in range(1,11):
    mult=i*num
    print(f"{num} X {i} = {mult}")

