package being.charlie.ding.cs61b.week2;

public class SortTest {

    public static boolean compareTwoArrayForString(String[] a1, String[] a2){
        boolean rs =true;
        for(int i=0;i<a1.length;i++){
            if(i > a2.length-1) {
                rs = false;
                break;
            }else{
               if(! a1[i].equals(a2[i])){
                 rs =false;
                   System.out.println(a1[i] +" not equal "+ a2[i]);
                 break;
               }
            }
        }
        return rs;
    }

    public static boolean compareTwoArrayForInt(int [] a1, int[] a2){
        boolean rs =true;
        for(int i=0;i<a1.length;i++){
            if(i > a2.length-1) {
                rs = false;
                break;
            }else{
                if(a1[i] != a2[i]){
                    rs =false;
                    System.out.println(a1[i] +" not equal "+ a2[i]);
                    break;
                }
            }
        }
        return rs;
    }



}
