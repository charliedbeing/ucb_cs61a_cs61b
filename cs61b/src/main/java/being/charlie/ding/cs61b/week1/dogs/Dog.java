package being.charlie.ding.cs61b.week1.dogs;

/**
 *  Class
 *  1: abstract  -> class == blueprint
 *     instance -> Object
 *
 *  2: resolve the complicity  =>
 *    separate which part belong to abstract(Class), which part belong to instance (Object)
 *  3: model the world into code world
 *  4:
 */
public class Dog {
    /** Each special dog should have personal feature: like weigh */
   public int weightOfDog;

   /** static field belong the blueprint level, share with all instances, which include created object and will be created  */
   public final static String typeOfDog ="pet";

   public static String unilName = " the power of smell";

    /** in order to create a special dog */
    public Dog(int weight){
        weightOfDog =weight;
    }

    public Dog(int weight, String type){
        weightOfDog=weight;
      //     typeOfDog = type; // if no final with static class field ,then this field can be changed,
        //   than may lead to the logic  errors.
    }

    public String getType(){
        return typeOfDog;
    }
    /** this method depend on the instance feature to work, so it must be instance method */
    public void makeNoice(){
        if(weightOfDog<=10){
            System.out.println("yapyap");
        }else if(weightOfDog<30){
            System.out.println("aoao");
        }else{
            System.out.println("hooooo");
        }
    }
/**1: it depend on the instance of Dog not the feature of a instance of Dog,so it can be not instance method
 * 2: From the logic view: Judge Dog instance should be happened in Class Level,
 *   because the Class is the blueprint of all instance of Dog
 *   blueprint can be look as the God of the Being of all the instance of Dog.
 *
 * 3: From the blueprint view offer a feature belong to the blueprint .
 * */
    public static Dog compareMoreHeavy(Dog d1,Dog d2){
        if (d1.weightOfDog>d2.weightOfDog){
            return d1;
        }else{
            return d2;
        }
    }
/** Give each instance a feature to compare with others */
    public Dog compareWithMe(Dog d){
        if(this.weightOfDog>d.weightOfDog){
            return this;
        }else{
            return d;
        }
    }

    @Override
    public String toString() {
        return "Dog{" +
                "weightOfDog=" + weightOfDog +
                '}';
    }
}
