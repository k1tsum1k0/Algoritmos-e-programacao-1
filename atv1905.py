#EX1
#  Faça um programa que leia uma frase e conte quantas vogais existemna frase
 
# entrada dos dados
frase=input().lower()

# declaração de variaveis uteis
vogais="aeiou"
cont=0

# looping para varer o vetor


for i in range(len(frase)):
    for j in range(len(vogais)):
        if(frase[i]==vogais[j]):
            cont+=1


print(cont)


# EX2
# codigo de leitura de uma matriz

# leitura da quantidade de linhas da mat# codigo de leitura de uma matriz

# leitura da quantidade de linhas da matriz
n=int(input())

# criação da matriz
matriz=[]

# para cada uma das linhas , faca a leitura
for i in range(n):

    linha=[]
    linha=list(map(int,input().split()))

    matriz.append(linha)

# imprime de diversas formas a matriz
for i in range(n):
    print(matriz[i])

for i in range(n):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()z
for i in range(n):
    print(matriz[i])

for i in range(n):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()








#EX1
#Faça um programa que leia o número de linhas e colunas de uma matriz. 
# Em seguida leia n linhas contendo m colunas cada e calcule o maior elemento da matriz

#entrada dos dados
n,m=input().split()

# conversão para inteiro
n=int(n)
m=int(m)

#declaração de variaveis
matriz=[]

#faz a leitura de todas as linhas
for i in range(n):
        linhas=[]
        linhas=list(map(int,input().split()))
        matriz.append(linhas)

# declaração da variavel maior
maior=matriz[0][0]

#compara todos os elementos da matriz para achar o maior
for j in range(n):
    for k in range(m):
        if maior<matriz[j][k]:
             maior=matriz[j][k]

# saida do resultado
print(maior)

#EX2
#Faça um programa que leia o  número de linhas e colunas de uma matriz. 
# Em seguida seu programa deve ler elementos da matriz. Por fim,calcule  a soma das linhas e das colunas da matriz.

#leitura das variaveis
n, m =input().split()

#conversao das variaveis
n=int(n)
m=int(m)

#declaração de variaveis uteis
matriz=[]

#leitura de todas as linhas
for i in range(n):
    linha=[]
    linha=list(map(int,input().split()))
    matriz.append(linha)

# soma de todas as linhas
for j in range(n):
    soma=0
    for k in range(m):
        soma+=matriz[j][k]

    # saida por linha    
    print(f"soma da linha {j}: {soma}")

# espaçamento entre as saidas
print("\n")

# soma de todas as colunas
for p in range(m):
    soma=0
    for q in range(n):
        soma+=matriz[q][p]

    # saida por coluna
    print(f"soma da coluna  {p}: {soma}")





#EX3
# Faça um programa que leia a dimensão de uma matriz quadrada nxn. Em seguida, leia os elementos da matriz. 
# Por fim, calcule a soma da diagonal principal e da diagonal secundária.

#entrada do tamanho da matriz quadrada
n=int(input())

#declaração de variaveis uteis
matriz=[[1, 4, 3],[2, 3, 7],[0, 5,9]]
diagprinc=0
diagsec=0

#looping que adiciona os elementos na matriz
#for i in range(n):
    #linha=[]
    #linha=list(map(int,input().split()))
    #matriz.append(linha)

#calcula a diagonal principal
for j in range(n):
    diagprinc+=matriz[j][j]

m=n

# calcula a diagonal secundaria
for k in range(n-1,0,-1):
    diagsec+=matriz[k][m]
    print(matriz[k][m])
    m-=m

    
print(f"soma da diagonal principal: {diagprinc}")
print(f"soma da diagonal secundaria: {diagsec}")
