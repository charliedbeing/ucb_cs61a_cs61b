package being.charlie.ding.cs61b;

import java.util.ArrayList;
import java.util.Arrays;

public class FindNumbers {

    private int[] numbers = {};

    public FindNumbers(int[] numbers){
        this.numbers = numbers;
    }

    public FindNumbers(){
        System.out.println("I am the default construct function for FindNumbers");

    }

    //  [10, 15, 20, 15, 10, 5, 10, 15, 22, 20]

    public ArrayList<Integer> find_number_helper(){


        ArrayList<Integer> result = new ArrayList<Integer>();

        for(int i=0;i<this.numbers.length;i++){
            if(is_number(i,result)){
                result.add(this.numbers[i]);
            }
        }


        return result;

    }

    //  [10, 15, 20, 15, 10, 5, 10, 15, 22, 20]

    /**
     *This method will return a new array that contains every Dog that is larger than
     * its 4 closest neighbors, i.e. the two on the left and the two in the right.
     * If there are not enough neighbors, i.e. you’re at the end of the array,
     * then consider just the neighbors that exist. For example:
     */

    private  boolean is_number(int index, ArrayList<Integer> result){
        boolean rs = false;
        int greater = 4;
        if (is_in_array(this.numbers[index],result)){
             rs=false ;
        }else{
            if (leftCount_two(index)+rightCount_two(index) == greater){
                rs=true;
            }
        }
        return rs;
    }

    private int leftCount_two(int index){
        int rs =0;
        if (index>1){
            if (this.numbers[index]>this.numbers[index-1]
                    && this.numbers[index]>this.numbers[index-2]){
                rs=2;
            }
        }
        return rs;
    }
    //  [10, 15, 20, 15, 10, 5, 10, 15, 22, 20]
    private int rightCount_two(int index){
        int rs =0;
        // 23 22 22
        // 23 22
        // 23
      if(index <= this.numbers.length-3){
          if (this.numbers[index]> this.numbers[index+1] &&
          this.numbers[index]>this.numbers[index+2]){
              rs=2;
          }
      }else if (index+1== this.numbers.length-1){
          if(this.numbers[index]>this.numbers[index+1]){
              rs=2;
          }
      }else if (index == this.numbers.length-1){
          rs=2;
      }

        return rs;
    }
    //  [10, 15, 20, 15, 10, 5, 10, 15, 22, 20]
    private int leftCount_common(int index){
        int rs =0;
        if(index >0){
            for(int i=0;i<index;i++){
                if (this.numbers[index] > this.numbers[i]){
                    rs+=1;
                }
            }
        }

        return rs;
    }
    //  [10, 15, 20, 15, 10, 5, 10, 15, 22, 20]

    private int rightCount(int index){
        int rs =0;
        if(index < this.numbers.length-1){
            for(int i=index+1; i<= this.numbers.length-1;i++){
                if ( this.numbers[index]>this.numbers[i]) {
                    rs+=1;
                }
            }
        }

        return rs;
    }

    private boolean is_in_array(int num, ArrayList<Integer> arr){

        return arr.contains(Integer.valueOf(num));

    }



    public static void main(String[] args) {
        System.out.println("HI, i am FindNumbers");
        int[] dogsize = {10, 15, 20, 15, 10, 5, 10, 15, 22, 20};

        dogsize= new int[]{10, 20, 30, 25, 20, 40, 10};
        FindNumbers findNumbers = new FindNumbers(dogsize);

        System.out.println(findNumbers.find_number_helper());

//        int[] a =new int[2];
//        System.out.println(a.length);
//        System.out.println(a[0]);


    }
}
