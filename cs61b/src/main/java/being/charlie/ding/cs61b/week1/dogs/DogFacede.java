package being.charlie.ding.cs61b.week1.dogs;

public class DogFacede {

    public static void main(String[] args) {

        Dog d1= new Dog(15);
        Dog d2 = new Dog(55);


        d1.makeNoice();

        d2.makeNoice();

        Dog.compareMoreHeavy(d1,d2).makeNoice();

    }
}
