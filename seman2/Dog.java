package seman2;

public class Dog {
    // atributos do dog
    String nome;
    int peso;

    // Metodos do dog
    public void latir(){
        if(peso>50){
            System.out.println("Woof! Woof! "+nome);

        }else if(peso>20){
            System.out.println("Ruff!! Ruff!! "+nome);
        }else{
            System.out.println("Yiip!! Yiip!! "+nome);
        }
    }
}
