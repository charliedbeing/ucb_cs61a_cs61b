package being.charlie.ding.cs61b.week1.hw0;

import java.util.ArrayList;

public  class FindNumbersTools {

    private static int[] numbers;

    public static void setNumbers(int[] numbs){
        numbers=numbs;
    }

    public static ArrayList<Integer> find_number_helper(){


        ArrayList<Integer> result = new ArrayList<Integer>();

        for(int i=0;i<numbers.length;i++){
            if(is_number(i,result)){
                result.add(numbers[i]);
            }
        }


        return result;

    }

    private static boolean is_number(int index, ArrayList<Integer> result){
        boolean rs = false;
        int greater = 4;
        if (is_in_array(numbers[index],result)){
            rs=false ;
        }else{
            if (leftCount_two(index)+rightCount_two(index) == greater){
                rs=true;
            }
        }
        return rs;
    }

    private static int leftCount_two(int index){
        int rs =0;
        if (index>1){
            if (numbers[index]>numbers[index-1]
                    && numbers[index]>numbers[index-2]){
                rs=2;
            }
        }
        return rs;
    }
    //  [10, 15, 20, 15, 10, 5, 10, 15, 22, 20]
    private static int rightCount_two(int index){
        int rs =0;
        // 23 22 22
        // 23 22
        // 23
        if(index <= numbers.length-3){
            if (numbers[index]> numbers[index+1] &&
                    numbers[index]>numbers[index+2]){
                rs=2;
            }
        }else if (index+1== numbers.length-1){
            if(numbers[index]>numbers[index+1]){
                rs=2;
            }
        }else if (index == numbers.length-1){
            rs=2;
        }

        return rs;
    }

    private static boolean is_in_array(int num, ArrayList<Integer> arr){

        return arr.contains(Integer.valueOf(num));

    }


}
