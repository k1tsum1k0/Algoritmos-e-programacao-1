/*Dados dois hor´arios de um mesmo dia, expressos no formato
hh:mm:ss, calcule o tempo decorrido entre estes dois hor´arios,
apresentando o resultado no mesmo formato hh:mm:ss.
Exemplo:
Se os dois hor´arios fornecidos s˜ao 07:13:22 e 13:05:56, a resposta tem de ser 05:52:34.*/

#include <stdio.h>

struct tipoData{
	int hh;
	int mm;
	int ss;
};

int main(){
	
	tipoData horario1, horario2, result;
	int segundos;


	scanf("%d:%d:%d",&horario1.hh,&horario1.mm,&horario1.ss);

	scanf("%d:%d:%d",&horario2.hh,&horario2.mm,&horario2.ss);

	segundos=(horario2.hh*3600+horario2.mm*60+horario2.ss)-(horario1.hh*3600+horario1.mm*60+horario1.ss);



	result.hh=(segundos/3600);
	result.mm=(segundos%3600)/60;
	result.ss=(segundos%3600)%60;



	printf("%d:%d:%d \n",result.hh,result.mm,result.ss);




	return 0;
}