# Faça um programa que leia um vetor de n elementos e em seguida leia um inteiro x. Por fim, seu programa deve multiplicar todos os elementos do vetor x.

#leitura do vetor de n elementos e x
vet=list(map(int, input().split()))
x=int(input())

#percorre o vetor e multiplica o valor por n imprimindo
for i in range(len(vet)):
    print(vet[i]*x, end=" ")
  
    # ouuuuu

# Faça um programa que leia um vetor de n elementos e em seguida leia um inteiro x. Por fim, seu programa deve multiplicar todos os elementos do vetor x.

#leitura do vetor de n elementos e x
vet=list(map(int, input().split()))
x=int(input())

#percorre o vetor e multiplica o valor por n
for i in range(len(vet)):
    vet[i]=vet[i]*x

# imprime o vetor
for i in range(len(vet)):
    print(vet[i],end=" ")



# Querendo saber se um dado é viciado,josemar anotou quantas vezes cada face de um dado saiu. 
# Faça um programa que leia a face sorteado de um dado lançado n vezes, até que o usuário digite -1.
# Em seguida, seu programa deve imprimir quantas vezes cada face caiu.

#inicialização das variaveis e vetores
face=[0]*6
x=int(input())


#leitura e contagem das faces dos dados armazenando n
while(x!=-1):
    face[x-1]=face[x-1]+1
    x=int(input())

#saida do vetor
for i in range(6):
    print(face[i], end=" ")



# Faça um programa que leia um vetor de n elementos e imprima os dois menores elementos.

#leitura do vetor
vet=list(map(int,input().split()))

#declaração das variaveis uteis
primeiromenor=1
segundomenor=0
aux=0

#laço para comparar os numeros e separar os dois maiores
for i in range(len(vet)):
    if vet[i]<vet[segundomenor]:
        vet[segundomenor]=i
    if vet[primeiromenor]>vet[segundomenor]:
        aux=primeiromenor
        primeiromenor=segundomenor
        segundomenor=aux

print(vet[primeiromenor],vet[segundomenor])

