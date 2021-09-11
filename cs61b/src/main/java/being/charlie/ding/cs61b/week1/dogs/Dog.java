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
    int weightOfDog;

    /** in order to create a special dog */
    public Dog(int weight){
        weightOfDog =weight;
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
 * */
    public static Dog compareMoreHeavy(Dog d1,Dog d2){
        if (d1.weightOfDog>d2.weightOfDog){
            return d1;
        }else{
            return d2;
        }
    }



}
