package being.charlie.ding.cs61a.scheme;

public class StringUtil {
    public static void main(String[] args) {

     test_1();


    }

    public static void test_1(){
        char[] chars = "(+ 2 3)".toCharArray();
        char[] chars1 =" ( -  2   3)".toCharArray();
        char[] chars12 =" ( -  2     (+ 2 3))".toCharArray();
        char[] chars122 ="(+ 2 (+ 2 3))".toCharArray();
//(+((+(- 4 2)(+ 2 3))(+ 2 3))
        char[] chars123 ="(+(+(+ 2 3)(- 3 2))(+ 2 3))".toCharArray();

        char[] chars2 ="( -  (+  44 5 )   3)".toCharArray();
        char[] chars3= "(+ (+ 2 3)    ( -  10   9))".toCharArray();
        char[] chars4= "(+ (+ 2 3)    ( -  (+ 123   390  )   9))".toCharArray();
        toRegularFormular(chars123);
    }

    /** get the most regular formular just must one space */
    public static String[] toRegularFormular(char[] chars){
        // iterator original charArray and  select correct char to new charArray.
        // operate black and deal with it
       // char[] chars = s.toCharArray();
        String [] res =null;
        char[] rs = removeExtraBlank(chars);
        res = transCharArrtoStrArr(rs);
        System.out.println(rs);

        String temp ="";
        for(int i=0;i<res.length;i++){
            temp = temp+res[i];
        }
        System.out.println(temp);
        return res;
    }

    /** rules:
     * 1: ( left and right remove => left all, right until operator
     * 2: from operator next space is keep , others remove until next not black should be number1 or (;
     * 3: number1 right space just keep one ,remove others until )
     * 4: ) left and right remove
     * 4:
     * ----------------
     * 1: ( ) left right all remove
     * 2: operator right just keep one when right is number, if when ( follow the ( rulers.
     * 3: number1 right just keep one when right is number is when ( follow the ( rulers
     */
    /**  only keep one situation: blank right is_number ;*/
    private static char[] removeExtraBlank(char [] chars){

        char[] rs = new char[chars.length];
        char blank =' ';
        int newIndex =0;

        for(int i=0;i<chars.length;i++){
            if(chars[i] == blank && is_right_number(chars,i)){
                rs[newIndex]= chars[i];
                newIndex = newIndex +1;
            }else if(chars[i]==blank){
                continue;
            }else {
                rs[newIndex]=chars[i];
                newIndex = newIndex+1;
            }
        }
        return getLegalCharArray(rs);
    }

    private static boolean is_right_number(char[] arr, int index){

        if(is_numbers(String.valueOf(arr[index+1]))){
            return true;
        }else{
            return false;
        }
    }


     public  static boolean  is_operator(String s){
        String [] operators ={"+","-","*","/"};
        return isIn(operators,s);
     }
    public static boolean is_bracket(String s){
        String [] brackets ={"(",")"};
        return isIn(brackets,s);
     }
    public static boolean is_numbers(String s){
        String [] numbers ={"0","1","2","3","4","5","6","7","8","9"};
        return isIn(numbers,s);
    }

    private static boolean legalChar(char c){
        boolean rs=false;
        String s = String.valueOf(c);
        if(is_numbers(s)||is_bracket(s)||is_operator(s)||' '==c){
            rs =true;
        }
        return rs;

    }

    private static char[] getLegalCharArray(char[] arr){
        int count =0;
        for(int i=0;i<arr.length;i++){
            if(legalChar(arr[i])){
                count =count+1;
            }
        }
        char[] rs = new char[count];
        for(int i=0; i<count;i++){
            rs[i]= arr[i];
        }
        return rs;
    }

    private static String[] getLegalStringArray(String[] arr){
        int count =0;
        for(int i=0;i<arr.length;i++){
            if(arr[i] != null ){
                count =count+1;
            }
        }
        String[] rs = new String[count];
        for(int i=0; i<count;i++){
            rs[i]= arr[i];
        }
        return rs;
    }

     /** Pure function  */
     private static boolean isIn(String[] arrs, String s){
        boolean rs =false;
        for(int i=0;i<arrs.length;i++){
            if(arrs[i].equals(s)){
                rs= true;
                break;
            }
        }
        return rs;
     }
// (- 2(+ 2 3))
     private static String[] transCharArrtoStrArr(char[] arr){
         String [] rs = new String[arr.length];

         int index =0;
         char blank = ' ';
         String temp = "";

         for(int i=0;i<arr.length;i++){

             if(is_numbers(String.valueOf(arr[i])))
             {
                 temp = temp+String.valueOf(arr[i]);

             }else
                 {
                     if(arr[i] == blank){
                         if(!temp.equals("")){
                             rs[index]= temp;
                             rs[index+1] = String.valueOf(arr[i]);
                             index= index+2;
                             temp="";
                         }else{
                             rs[index] = String.valueOf(arr[i]);
                             index = index +1;
                         }
                     }else if(is_operator(String.valueOf(arr[i])) || String.valueOf(arr[i]).equals("(")){
                         if(String.valueOf(arr[i]).equals("(")){
                             if(!temp.equals("")){
                                 rs[index]= temp;
                                 rs[index+1] = String.valueOf(arr[i]);
                                 index= index+2;
                                 temp="";
                             }else{
                                 rs[index] = String.valueOf(arr[i]);
                                 index = index +1;
                             }
                         }else{
                             rs[index] = String.valueOf(arr[i]);
                             index = index +1;
                         }

                     }else if( String.valueOf(arr[i]).equals(")")){
                         if(!temp.equals("")){
                             rs[index]= temp;
                             rs[index+1] = String.valueOf(arr[i]);
                             index= index+2;
                             temp="";
                         }else{
                             rs[index] = String.valueOf(arr[i]);
                             index = index +1;
                         }

                     }
                 }

         }


         return getLegalStringArray(rs);
     }

     private static String[] transCharArrayToStringArray(char[] arr){
         String [] rs = new String[arr.length];

         int index =0;
         char blank = ' ';
         String temp = "";


         for(int i=0;i<arr.length;i++){
            if(is_numbers(String.valueOf(arr[i]))){
                // first number
                if(arr[i-1] == blank && arr[i+1] ==blank){
                    rs[index] = String.valueOf(arr[i]);
                    index = index +1;
                }else if(arr[i-1] == blank && is_numbers(String.valueOf(arr[i+1]))  ){
                    temp = temp+ String.valueOf(arr[i]);
                    continue;
                }else if(is_numbers(String.valueOf(arr[i]))&& arr[i+1]!= blank){
                    temp = temp+ String.valueOf(arr[i]);
                    continue;
                }else if(is_numbers(String.valueOf(arr[i]))&& arr[i+1] == blank){
                    temp = temp+ String.valueOf(arr[i]);
                    rs[index] =temp;
                    index = index+1;
                    temp="";
                }
                // second number
                else if(arr[i-1] ==blank && is_bracket(String.valueOf(arr[i+1]))){
                    rs[index] = String.valueOf(arr[i]);
                    index = index +1;

                }else if( arr[i-1] == blank && !is_bracket(String.valueOf(arr[i+1]))){
                    temp = temp+ String.valueOf(arr[i]);
                    continue;

                }else if(is_numbers(String.valueOf(arr[i]))&& !is_bracket(String.valueOf(arr[i+1]))){
                    temp = temp+ String.valueOf(arr[i]);
                    continue;
                }else if(is_numbers(String.valueOf(arr[i]))&& is_bracket(String.valueOf(arr[i+1]))){
                    temp = temp+ String.valueOf(arr[i]);
                    rs[index] =temp;
                    index = index+1;
                    temp="";
                }

            }else{
                rs[index] = String.valueOf(arr[i]);
                index = index +1;
            }
         }

         return rs;
     }

}











