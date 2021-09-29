package being.charlie.ding.cs61a.scheme;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Try to parse (+ 2 3) => 5
 */

/** Stack Tool Class */
class SStack{

    private  String[] container= new String[100];
    private  int index=0;

    public int getCurr(){
        return index;
    }
    public   void  push(String s){
        if(index == container.length-1){
            String [] temp = new String[container.length*2];
            for(int i=0;i < container.length;i++){
                temp[i]=container[i];
            }
            container = temp;
        }
        container[index]=s;
        index =index+1;
    }

    public  String pop(){
        int curr = index -1;
        String s="";
        if(curr>=0){
            s= container[curr];
            index = index -1;
        }
        return s;
    }
    public void clear(){
        container = new String[100];
        index =0;
    }

}

public class Parse_Operation {

    public static void main(String[] args) {

      testM1();
    }

    /** Main function test */

    private static void testM1(){
        String s2 = "(+ (- 4 2) (* 3 2))";
        String s3 = "(+ (- 4 1) (/ 9 3))";
        int rs = parseHelp(s3);

        System.out.println(rs == 33 );
    }

    /** some test for basic function */
    private static void test3(){
        // test2();
//        SStack s = new SStack();
//            s.push("(");
//            s.push("2");
//
//        System.out.println(s.pop());

        // System.out.println(  parseHelp("ss")) ;

    }

    private static void test2(){
        String s1=  "(+ 2 3)";
        String s2 = "(+ (- 4 2) (* 3 4))";

        char[] s1_trans = s1.toCharArray();
        char[] s2_trans = s2.toCharArray();
        return;

    }

    private static void test1(){
        String s= "(+  (+ 2 3)  (- 10 9))";
        String[] ss = s.split(" ");
        Arrays.stream(ss).forEach(System.out::println);

        s = s.replace("  "," ");

        System.out.println(s);
    }

    private String[] compressSpaceblack(String[] acc){
        String[] rs = new String[acc.length];

        for(int i=0;i<acc.length;i++){

        }

        return null;
    }
    /** End of some test for basic function */

    /**
     * (+ 2 3)
     * (+ (- 4 2) (* 3 4))
     * String[] container c;
     * c[0]='('
     * c[1]='+' all accepted operators
     * c[2]=' ' if more than one '' => one ''
     * c[3]='2' can be another formula
     * c[4]=' ' if more than one '' => one ''
     * c[5]='3' can be another formula
     * c[6]=')'
     */

    public static int parseHelp(String formula){
        // 1: get operator
        // 2: get leftItem and rightItem
        //    2.1: leftItem is value or  parseHelp(s_leftItem) ; rightItem is value or parseHelp(s_rightItem)
        // 3: call f_op(operator, leftItem, rightItem)
        String[] s = getStringArrayFromCharArray(formula.toCharArray());

        String operator = getOperator(s);
        String leftItem = getLeftItem(s);
        String rightItem = getRightItem(s);


        return f_op(operator,leftItem,rightItem);
    }

    /** Three part funciton to server parseHelp  */
    private static String getOperator(String [] s){

        return s[1];

    }
    private static String getLeftItem(String[]s){

        String rs ="";
        String left = s[3] ;
        if(! left.equals("(")){
            rs = left;
        }else{
            rs = leftItemHelp(s,3)[0];
        }

        return rs;
    }

    private static String getRightItem(String[] s){

        String rs ="";
        String left = s[3];

        if(! left.equals("(")){
            rs = s[5];;

        }else{
            int index  =Integer.parseInt(leftItemHelp(s,3)[1]);
            rs = leftItemHelp(s,index+1 )[0];
        }

        return rs;
    }


/** some help methods to server three part function  */
    private static String[] leftItemHelp(String[] charArray,int index){
        String[] rs = new String [2];
        SStack s = new SStack();

        if(charArray[index].equals("(")){
            int rightIndex = index;
            s.push(String.valueOf(index));

            for(int i=index+1;i<charArray.length;i++){

                if("(".equals(String.valueOf(charArray[i]))){
                    s.push(String.valueOf(i));
                }else if(")".equals(String.valueOf(charArray[i]))){
                    if(s.getCurr() ==1){
                        rightIndex = i;
                        break;
                    }else{
                        s.pop();
                    }
                }else{
                    continue;
                }
            }

            rs[0] = getPartFromCharArray(index, rightIndex,charArray);
            rs[1] = String.valueOf(rightIndex);
        }else{
            rs[0]=charArray[index+1];
            rs[1]= String.valueOf(index+1);
        }


        return rs;
    }

    private static String getPartFromCharArray(int begin,int end, String [] chars){
        String s ="";
        for(int i= begin;i<= end;i++){
            s= s+ chars[i];
        }
        return s;
    }



    private static int f_op(String operator, String leftItem, String rightItem){
        int leftItem_int =0;
        int rightItem_int =0;

        if(leftItem.startsWith("(")){
            leftItem_int = parseHelp(leftItem);
        }else{
            leftItem_int = Integer.parseInt(leftItem);
        }

        if(rightItem.startsWith("(")){
            rightItem_int = parseHelp(rightItem);
        }else{
            rightItem_int = Integer.parseInt(rightItem);
        }

        return simple_op(operator,leftItem_int,rightItem_int);
    }

    private static int simple_op(String op, int left,int right){
        int rs =0 ;
        if(op.equals("+")){
            rs= left +right;
        }else if(op.equals("-")){
            rs=  left- right;
        }else if(op.equals("*")){
            rs=  left * right;
        }else if(op.equals("/")){
            rs=  left / right;
        }

        return rs;
    }


    /**  pure basic function methods*/

    private static String[] getStringArrayFromCharArray(char [] chars){
        String[] r = new String[chars.length];
        for(int i=0;i<r.length;i++){
            r[i] = String.valueOf(chars[i]);
        }
        return r;
    }


    private String[] parseFormula(String s){

        return null;
    }

}
