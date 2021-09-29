package being.charlie.ding.cs61b.week2.link.lect;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
public class SortLect {

    /** Sorts strings destructively */
    public static void sort(String[] x){

        // Find the smallest item
        // Move it to the front
        // Selection sort the rest (using recursion ??)

        /** strategy 1: iterator */
//        for(int i=0;i<x.length;i++){
//            int sm_index = getSmallestInArrary(i,x);
//            swapTwoWordInArray(i,sm_index,x);
//        }
        /** strategy 2: recursive */

        sort_help_2(x,0);

    }

    public static void sort_2(String[] x){

        int first_index = getSmallestInArrary(0,x);
        swapTwoWordInArray(0,first_index,x);

    }

    private static void sort_help(String[]x,int index){
        if(index == x.length){
            return ;
        }else{
            int curr = getSmallestInArrary(index,x);
            swapTwoWordInArray(curr,index,x);
            sort_help(x,index+1);
        }
    }

    private static void sort_help_2(String[]x,int index){
        if(index == x.length){
            return ;
        }
            int curr = getSmallestInArrary(index,x);
            swapTwoWordInArray(curr,index,x);
            sort_help_2(x,index+1);

    }

    /** step_1:  return from beginIndex to the end , the postion of the smallest */
    private static int getSmallestInArrary(int beginIndex,String[] arr){

        int sm =97+25+1;
        int currIndex=beginIndex;

        for(int i=beginIndex;i<= arr.length-1;i++){
            int curr = wordToInt(arr[i]);
            if(curr < sm){
                 sm =curr;
                currIndex= i;
            }
        }

        return currIndex;
    }

    /** step_2 Move it to the front => swap */
    private static void swapTwoWordInArray(int frontPosition,int rearPosition,String[]arr){
        String temp = arr[frontPosition];
        arr[frontPosition] =arr[rearPosition];
        arr[rearPosition] = temp;
    }

    /** step_3 finish the rest 1_ iterator*/

    private static void finishTheRest(int currIndex, String[] arr){
        int sm_index = getSmallestInArrary(currIndex,arr);
        swapTwoWordInArray(currIndex,sm_index,arr);
    }



    public static void main(String[] args) {
       // test_getSmallest();
        // test_sort();
        SortLect s = new SortLect();
        s.test_sort();
    }

    private static void test_1(){
        char a='a';
        int a_int = a;
        String r="";
        for(int i=97;i<= 97+25;i++){
            char temp = (char) i;
            r = r+temp;

        }

        System.out.println(wordToInt("apple"));
    }

    private static void test_getSmallest(){
        String[] s1 ={"zoo","apple","bed","able"};

        System.out.println(getSmallestInArrary(2,s1) == 3);
    }

    @Test
    void test_sort(){
        String[] s1 ={"zoo","apple","bed","able"};
        String [] s2 ={"apple","able","bed","zoo"};
        sort(s1);
        assertArrayEquals(s2,s1);
    }

    private static int wordToInt(String w){
        String rs = w.toLowerCase();
        char first = rs.charAt(0);
        int r = (int)first;
        return r;
    }

}

