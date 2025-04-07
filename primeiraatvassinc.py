
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