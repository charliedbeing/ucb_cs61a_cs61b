package being.charlie.ding.cs61b.week1.dogs;

import java.util.ArrayList;

public class DogFacede {

    public static void main(String[] args) {

    // test0();
    test1();


    }

    public static void test0(){
        Dog d1= new Dog(15);
        Dog d2 = new Dog(55);


        Dog d3= new Dog(199,"wild");

        d1.makeNoice();

        d2.makeNoice();

        Dog.compareMoreHeavy(d1,d2).makeNoice();

        System.out.println(Dog.typeOfDog);

        System.out.println(d1.getType());

        System.out.println(d3.getType());

        System.out.println(Dog.unilName);
    }

    public static void  test1(){
        Dog[] dogs = new Dog[3];

        ArrayList<Dog> dogArrayList = new ArrayList<Dog>();
        System.out.println(dogs[0]);
        System.out.println(dogs.length);
        System.out.println(dogArrayList.size());
        dogArrayList.add(new Dog(1));
        System.out.println(dogArrayList.get(0));

    }
}
