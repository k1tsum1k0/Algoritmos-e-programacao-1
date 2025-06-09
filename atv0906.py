# entrada da qtt de linhas e colunas
n=int(input())

# declaração da matriz
matriz=[]

#entrada dos numero na matriz
for i in range(n):
    matriz.append(list(map(int,input().split())))

# saida da matriz m
for j in range(n):
    for k in range(j+1):
        print(matriz[j][k],end=" ")
    print()


# ex 2

#entrada de dois numeros inteiros n e m
n,m=map(int,input().split())

# declaração de variaveis uteis
filial=[]
total=0
totalvendaloja=[]
totalvendames=[]

#entrada dos dados das filiais
for i in range(n):
    filial.append(list(map(int,input().split())))


for j in range(n):
    for k in range(m):
        total+=filial[j][k]
    print(total,end=" ")
    totalvendaloja.append(total)
    total=0


print()
total=0
for p in range(m):
    for q in range(n):
        total+=filial[q][p]
    print(total,end=" ")
    totalvendames.append(total)
    total=0

print()
menor=0
for b in range(1,len(totalvendaloja)):
    if totalvendaloja[menor]>totalvendaloja[b]:
        menor=b

print(f"Loja  {menor+1}")

mes=0
menor=0

for r in range(n):
    for s in range(m):
        if filial[menor][mes]>filial[r][s]:
            menor=r
            mes=s

if mes==0:
    print(f"Mês de menor venda: Janeiro. Loja: {menor+1}.")
elif mes==1:
    print(f"Mês de menor venda: Fevereiro. Loja: {menor+1}.")
elif mes==2:
    print(f"Mês de menor venda: Março. Loja: {menor+1}.")
elif mes==3:
    print(f"Mês de menor venda: Abril. Loja: {menor+1}.")
elif mes==4:
    print(f"Mês de menor venda: Maio. Loja: {menor+1}.")
else:
    print(f"Mês de menor venda: Junho. Loja: {menor+1}.")

# ex 3

# COMMMM ERROOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!
# ex3:

# entrada da qtd de linhas
n=int(input())

matriz=[[1],[1,1]]
linha=[]
aux=0

print(1)
for i in range(n):
    for j in range(n+1):
        if j==0 or i==len(matriz):
            linha.append(1)
    linha.append(matriz[i][i+1])
    

for i in range(len(matriz)):
    for j in range(i+1):
        print(matriz[i][j],end=" ")
    print()