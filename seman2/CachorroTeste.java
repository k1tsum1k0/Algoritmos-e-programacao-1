package seman2;
public class CachorroTeste{
    public static void main(String[] args){
        Dog d1= new Dog();
        Dog d2 = new Dog();
        Dog d3= new Dog();

        d1.nome= "Amora";
        d1.peso = 90;

        d2.nome= "Joana";
        d2.peso=30;

        d3.nome ="Talisom";
        d3.peso = 2;

        d1.latir();
        d2.latir();
        d3.latir();


    }
}